const LIMIT: usize = 10_000_000;

fn run_sieve() -> usize {
    let mut is_prime = vec![true; LIMIT + 1];
    is_prime[0] = false;
    is_prime[1] = false;

    // Sieve
    let sqrt_limit = (LIMIT as f64).sqrt() as usize;
    for p in 2..=sqrt_limit {
        if is_prime[p] {
            let mut i = p * p;
            while i <= LIMIT {
                is_prime[i] = false;
                i += p;
            }
        }
    }

    is_prime.iter().filter(|&&x| x).count()
}

fn main() {
    let count = run_sieve();
    println!("Count: {}", count);
}
