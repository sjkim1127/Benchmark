import subprocess
import time
import os
import json
import sys
import re

# Configuration
ITERATIONS = 3 # Reduced to 3 to save time given many benchmarks

BENCHMARKS = [
    {
        "id": "sieve",
        "name": "Prime Sieve (CPU/Memory)",
        "expected": "Count: 664579"
    },
    {
        "id": "fibonacci",
        "name": "Fibonacci (Recursion/Stack)",
        "expected": "Result: 102334155"
    },
    {
        "id": "binary_tree",
        "name": "Binary Tree (Alloc/GC)",
        "expected": "Tree allocated"
    },
    {
        "id": "word_count",
        "name": "Word Count (String/Hash)",
        "expected": "Unique"
    },
    {
        "id": "matrix_mul",
        "name": "Matrix Mul (Numeric)",
        "expected": "Done"
    },
    {
        "id": "concurrency",
        "name": "Concurrency (Spawn)",
        "expected": "Done"
    },
    {
        "id": "mandelbrot",
        "name": "Graphics (Mandelbrot)",
        "expected": "Done"
    }
]

LANGUAGES = [
    {
        "name": "C",
        "subdir": "c",
        "build_cmd": ["make"],
        "run_cmd": ["./main"],
        "clean_cmd": ["make", "clean"]
    },
    {
        "name": "C++",
        "subdir": "cpp",
        "build_cmd": ["make"],
        "run_cmd": ["./main"],
        "clean_cmd": ["make", "clean"]
    },
    {
        "name": "Rust",
        "subdir": "rust",
        "build_cmd": ["cargo", "build", "--release"],
        "run_cmd": ["./target/release/"],
        "clean_cmd": ["cargo", "clean"]
    },
    {
        "name": "Go",
        "subdir": "go",
        "build_cmd": ["go", "build", "-o", "main", "main.go"],
        "run_cmd": ["./main"],
        "clean_cmd": ["rm", "-f", "main"]
    },
    {
        "name": "Swift",
        "subdir": "swift",
        "build_cmd": ["make"],
        "run_cmd": ["./main"],
        "clean_cmd": ["make", "clean"]
    },
    {
        "name": "Java",
        "subdir": "java",
        "build_cmd": ["make"],
        "run_cmd": ["java", "Main"],
        "clean_cmd": ["make", "clean"]
    },
    {
        "name": "Zig",
        "subdir": "zig",
        "build_cmd": ["make"],
        "run_cmd": ["./main"],
        "clean_cmd": ["make", "clean"]
    },
    {
        "name": "Python",
        "subdir": "python",
        "build_cmd": None,
        "run_cmd": ["python3", "main.py"],
        "clean_cmd": None
    },
    {
        "name": "Python++",
        "subdir": "python_optimized",
        "build_cmd": None,
        "run_cmd": ["python3", "main.py"],
        "clean_cmd": None
    },
    {
        "name": "JavaScript",
        "subdir": "javascript",
        "build_cmd": None,
        "run_cmd": ["node", "main.js"],
        "clean_cmd": None
    },
    {
        "name": "Assembly",
        "subdir": "assembly",
        "build_cmd": ["make"],
        "run_cmd": ["./main"],
        "clean_cmd": ["make", "clean"]
    }
]

def run_command(cmd, cwd):
    try:
        subprocess.run(cmd, cwd=cwd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        # Ignore clean errors
        if "clean" in cmd: return
        print(f"Error running command {' '.join(cmd)} in {cwd}: {e.stderr.decode()}")
        # Don't exit, just skip
        raise e

def get_rust_binary_path(path):
    try:
        with open(os.path.join(path, "Cargo.toml"), "r") as f:
            for line in f:
                if line.startswith("name ="):
                    name = line.split("=")[1].strip().strip('"').strip("'")
                    return os.path.join("./target/release", name)
    except:
        pass
    return None

class PowerSampler:
    def __init__(self):
        self.process = None
    
    def start(self):
        try:
            # We sample at 250ms for better granularity during short tests
            self.process = subprocess.Popen(
                ["sudo", "-n", "powermetrics", "-i", "250", "--show-cpu-power", "--show-gpu-power"],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                text=True
            )
        except:
            self.process = None

    def stop(self):
        if not self.process: return 0
        self.process.terminate()
        try:
            stdout, _ = self.process.communicate(timeout=2)
            # Find mW values for CPU/Combined Power
            matches = re.findall(r"(?:CPU|Package|Combined|ANE) Power:?\s*(\d+)\s*mW", stdout)
            if matches:
                powers = [float(m) for m in matches]
                # Filter out zeroes and take average
                powers = [p for p in powers if p > 0]
                if powers:
                    return (sum(powers) / len(powers)) / 1000.0 # Watts
        except:
            pass
        return 0

def run_benchmark(bench, lang, power_available):
    bench_dir = os.path.join("benchmarks", bench["id"], lang["subdir"])
    if not os.path.exists(bench_dir):
        return None

    print(f"  [{lang['name']}] Building...")
    if lang["clean_cmd"]:
        try: run_command(lang["clean_cmd"], bench_dir)
        except: pass

    if lang["build_cmd"]:
        try:
            run_command(lang["build_cmd"], bench_dir)
        except subprocess.CalledProcessError:
            print(f"    Build failed for {lang['name']}")
            return None

    run_cmd = list(lang["run_cmd"])
    if lang["name"] == "Rust":
        bin_path = get_rust_binary_path(bench_dir)
        if bin_path: run_cmd = [bin_path]
        else: return None

    times = []
    mem_usages = []
    energy_samples = []
    
    print(f"  [{lang['name']}] Running...")
    
    for i in range(ITERATIONS):
        sampler = PowerSampler() if power_available else None
        if sampler: sampler.start()
        
        start = time.time()
        try:
            time_cmd = ["/usr/bin/time", "-l"] + run_cmd
            result = subprocess.run(time_cmd, cwd=bench_dir, capture_output=True, text=True, check=True)
            duration = time.time() - start
            times.append(duration)
            
            avg_power = sampler.stop() if sampler else 0
            if avg_power > 0:
                energy_samples.append(avg_power * duration)
            
            stderr = result.stderr
            peak_rss = 0
            for line in stderr.splitlines():
                if "maximum resident set size" in line:
                    parts = line.strip().split()
                    if parts:
                        peak_rss = int(parts[0]) / (1024 * 1024)
                    break
            mem_usages.append(peak_rss)

            output = result.stdout.strip()
            if bench["expected"] not in output:
                if bench["id"] == "concurrency": pass
                else: print(f"    Warning: Unexpected output: {output[:50]}...")
        except subprocess.CalledProcessError as e:
            print(f"    Run failed: {e.stderr}")
            if sampler: sampler.stop()
            return None

    avg_time = sum(times) / len(times)
    avg_mem = sum(mem_usages) / len(mem_usages)
    avg_energy = sum(energy_samples) / len(energy_samples) if energy_samples else 0
    return avg_time, avg_mem, avg_energy

def main():
    power_available = False
    try:
        subprocess.run(["sudo", "-n", "true"], check=True, capture_output=True)
        power_available = True
        print("[INFO] Power measurement enabled (sudo available)")
    except:
        print("[WARN] Power measurement disabled (sudo password required). Run with 'sudo' for Energy metrics.")

    final_results = {}

    for bench in BENCHMARKS:
        print(f"\n=== Benchmark: {bench['name']} ===")
        results = []
        for lang in LANGUAGES:
            res = run_benchmark(bench, lang, power_available)
            if res is not None:
                avg_time, avg_mem, avg_energy = res
                results.append((lang["name"], avg_time, avg_mem, avg_energy))
        
        results.sort(key=lambda x: x[1])
        final_results[bench["name"]] = results
        
        print(f"\n--- Results: {bench['name']} ---")
        print(f"{'Language':<15} | {'Time (s)':<8} | {'Mem (MB)':<8} | {'Energy (J)':<8}")
        print("-" * 55)
        for name, t, m, e in results:
            e_str = f"{e:.2f}" if e > 0 else "-"
            print(f"{name:<15} | {t:.3f}    | {m:.1f}     | {e_str}")

    json_data = {}
    for bench_name, results in final_results.items():
        json_data[bench_name] = {lang: [t, m, e] for lang, t, m, e in results}
    
    with open("results.json", "w") as f:
        json.dump(json_data, f, indent=2)
    print("\nResults saved to results.json")

    print("\n\n" + "="*80)
    print("                FINAL SUMMARY (Time(s) / Energy(J))")
    print("="*80)
    
    header = f"{'Benchmark':<25}"
    lang_names = [l["name"] for l in LANGUAGES]
    for ln in lang_names:
        header += f" | {ln[:4]:<7}"
    print(header)
    print("-" * len(header))

    for bench in BENCHMARKS:
        row = f"{bench['name']:<25}"
        res_map = {name: (t, m, e) for name, t, m, e in final_results.get(bench["name"], [])}
        for ln in lang_names:
            val = res_map.get(ln, None)
            if val is not None:
                t, _, e = val
                e_val = f"{e:.1f}" if e > 0 else "n/a"
                row += f" | {t:.1f}/{e_val}"
            else:
                row += f" | {'-':<7} "
        print(row)

if __name__ == "__main__":
    main()
