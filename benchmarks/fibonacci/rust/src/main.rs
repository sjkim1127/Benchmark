fn fib(n: u32) -> u64 {
    if n <= 1 {
        return n as u64;
    }
    fib(n - 1) + fib(n - 2)
}

fn main() {
    let n = 40;
    let result = fib(n);
    println!("Result: {}", result);
}
