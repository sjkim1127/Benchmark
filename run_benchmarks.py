import subprocess
import time
import os
import sys

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
        "expected": "Unique words: 20"
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
        "run_cmd": ["./target/release/"], # Binary name depends on cargo.toml
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
        "name": "Python",
        "subdir": "python",
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
    # Try to find binary in target/release/
    # Name is usually project name
    try:
        with open(os.path.join(path, "Cargo.toml"), "r") as f:
            for line in f:
                if line.startswith("name ="):
                    name = line.split("=")[1].strip().strip('"').strip("'")
                    # Return path relative to the benchmark directory (which is 'path')
                    return os.path.join("./target/release", name)
    except:
        pass
    return None

def run_benchmark(bench, lang):
    bench_dir = os.path.join("benchmarks", bench["id"], lang["subdir"])
    if not os.path.exists(bench_dir):
        return None # Skip if not implemented

    print(f"  [{lang['name']}] Building...")
    
    # Clean first
    if lang["clean_cmd"]:
        try:
            run_command(lang["clean_cmd"], bench_dir)
        except: pass

    # Build
    if lang["build_cmd"]:
        try:
            run_command(lang["build_cmd"], bench_dir)
        except subprocess.CalledProcessError:
            print(f"    Build failed for {lang['name']}")
            return None

    # Determine run command
    run_cmd = list(lang["run_cmd"])
    if lang["name"] == "Rust":
        bin_path = get_rust_binary_path(bench_dir)
        if bin_path:
            run_cmd = [bin_path]
        else:
            print("    Could not find Rust binary")
            return None

    times = []
    print(f"  [{lang['name']}] Running...")
    
    for i in range(ITERATIONS):
        start = time.time()
        try:
            result = subprocess.run(run_cmd, cwd=bench_dir, capture_output=True, text=True, check=True)
            end = time.time()
            duration = end - start
            times.append(duration)
            
            output = result.stdout.strip()
            if bench["expected"] not in output:
                 # Special case for concurrency with 1000 threads (C/C++)
                 if bench["id"] == "concurrency" and "Counter: 1000" in output:
                     pass # Acceptable
                 elif bench["id"] == "concurrency" and "Counter: 100000" in output:
                     pass # Acceptable
                 else:
                     print(f"    Warning: Unexpected output: {output[:50]}...")
        except subprocess.CalledProcessError as e:
            print(f"    Run failed: {e.stderr}")
            return None

    avg_time = sum(times) / len(times) if times else 0
    return avg_time

def main():
    final_results = {}

    for bench in BENCHMARKS:
        print(f"\n=== Benchmark: {bench['name']} ===")
        results = []
        for lang in LANGUAGES:
            avg_time = run_benchmark(bench, lang)
            if avg_time is not None:
                results.append((lang["name"], avg_time))
        
        results.sort(key=lambda x: x[1])
        final_results[bench["name"]] = results
        
        print(f"\n--- Results: {bench['name']} ---")
        print(f"{'Language':<15} | {'Time (s)':<10}")
        print("-" * 28)
        for name, t in results:
            print(f"{name:<15} | {t:.4f}")

    # Final summary table
    print("\n\n=======================================================")
    print("                FINAL SUMMARY (Time in s)")
    print("=======================================================")
    
    # Header
    header = f"{'Benchmark':<25}"
    lang_names = [l["name"] for l in LANGUAGES]
    for ln in lang_names:
        header += f" | {ln:<8}"
    print(header)
    print("-" * len(header))

    for bench in BENCHMARKS:
        row = f"{bench['name']:<25}"
        res_map = dict(final_results.get(bench["name"], []))
        for ln in lang_names:
            val = res_map.get(ln, None)
            if val is not None:
                row += f" | {val:.4f}  "
            else:
                row += f" | {'-':<8}  "
        print(row)

if __name__ == "__main__":
    main()
