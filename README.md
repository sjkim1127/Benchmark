# Multi-Language Speed Benchmark

A comparative study of programming language performance across various algorithmic domains.

## 💻 Environment

- **Chip**: Apple M4 Pro (ARM64)
- **OS**: macOS
- **Architecture**: ARM64

## 🏆 Supported Languages

- **C** (GCC/Clang) - The Baseline
- **C++** (G++/Clang++) - Standard with `std::vector`
- **Rust** (Cargo) - Systems Programming, Safety
- **Go** (Golang) - Garbage Collection, Concurrency
- **Python** (CPython) - Interpreted
- **JavaScript** (Node.js) - JIT compiled (V8)
- **Assembly** (ARM64) - Handwritten Native Code

## 🧪 Benchmarks

We tested 6 different computational domains:

1. **Prime Sieve (CPU/Memory)**: Sieve of Eratosthenes (up to 10M). Tests tight loops and memory access.
2. **Fibonacci (Recursion)**: `fib(40)` using naive recursion. Tests stack overhead and function calls.
3. **Binary Tree (Memory/GC)**: Allocate/Deallocate full binary tree of depth 20. Tests allocator and GC speed.
4. **Word Count (String)**: Frequency count of words in a 50MB generated file. Tests string hashing and map performance.
5. **Matrix Multiplication (Numeric)**: 512x512 matrix multiplication. Tests numeric throughput and potential vectorization.
6. **Concurrency**: Spawning 100k tasks/threads. Tests context switching and scheduler overhead.
7. **Graphics (Mandelbrot)**: Generate 2048x2048 fractal. Tests floating-point arithmetic.

## 🚀 How to Run

1. Ensure you have all compilers installed (`gcc`, `g++`, `rustc`, `go`, `python3`, `node`).
2. Run the orchestrator script:

    ```bash
    python3 run_benchmarks.py
    ```

## 📊 Key Findings (M4 Pro)

*Results may vary by run, but general trends observed:*

- **JavaScript (Node.js/V8)** is remarkably fast, often beating C/C++ in memory allocation (Binary Tree) and auto-vectorized numeric tasks (Sieve, Matrix) due to JIT optimizations.
- **Rust** dominates in system-heavy tasks like String processing and HashMaps.
- **C/C++** remain the kings of raw function call performance (Fibonacci), beating even handwritten Assembly.
- **Python** is generally slower but can perform decently with idiomatic optimizations (e.g., slice assignment).
- **Handwritten Assembly** is not guaranteed to be faster than `-O3` optimized C/C++.

## License

MIT
