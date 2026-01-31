#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Configuration
#define LIMIT 10000000

int run_sieve() {
    // 0 and 1 are not primes, so we need LIMIT + 1 size
    // Using simple boolean array (char in C)
    // 1 (true) means prime, 0 (false) means not prime
    char *is_prime = (char *)malloc((LIMIT + 1) * sizeof(char));
    if (is_prime == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return -1;
    }

    // Initialize all to true (1)
    for (int i = 0; i <= LIMIT; i++) {
        is_prime[i] = 1;
    }

    is_prime[0] = 0;
    is_prime[1] = 0;

    for (int p = 2; p * p <= LIMIT; p++) {
        // If is_prime[p] is not changed, then it is a prime
        if (is_prime[p] == 1) {
            // Update all multiples of p
            for (int i = p * p; i <= LIMIT; i += p)
                is_prime[i] = 0;
        }
    }

    int count = 0;
    for (int p = 2; p <= LIMIT; p++) {
        if (is_prime[p]) {
            count++;
        }
    }

    free(is_prime);
    return count;
}

int main() {
    int count = run_sieve();
    printf("Count: %d\n", count);
    return 0;
}
