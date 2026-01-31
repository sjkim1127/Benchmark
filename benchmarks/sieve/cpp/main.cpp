#include <iostream>
#include <vector>
#include <cmath>

// Configuration
const int LIMIT = 10000000;

int run_sieve() {
    // std::vector<bool> is a space-efficient specialization
    // It uses 1 bit per boolean, which is memory efficient
    // but might be slightly slower due to bitwise operations compared to char array
    // However, for idiomatic C++, it's the standard way.
    std::vector<bool> is_prime(LIMIT + 1, true);

    is_prime[0] = false;
    is_prime[1] = false;

    // Sieve
    // We can iterate up to sqrt(LIMIT)
    int sqrt_limit = std::sqrt(LIMIT);
    for (int p = 2; p <= sqrt_limit; ++p) {
        if (is_prime[p]) {
            for (int i = p * p; i <= LIMIT; i += p) {
                is_prime[i] = false;
            }
        }
    }

    int count = 0;
    for (int p = 2; p <= LIMIT; ++p) {
        if (is_prime[p]) {
            count++;
        }
    }

    return count;
}

int main() {
    // std::cout synchronization might slow things down if printing a lot,
    // but here we only print once.
    std::ios_base::sync_with_stdio(false); 
    int count = run_sieve();
    std::cout << "Count: " << count << std::endl;
    return 0;
}
