
import numpy as np
import time

def sieve(limit):
    isPrime = np.ones(limit + 1, dtype=bool)
    isPrime[0:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if isPrime[p]:
            isPrime[p*p : limit+1 : p] = False
    return np.count_nonzero(isPrime)

def main():
    limit = 10_000_000
    count = sieve(limit)
    print(f"Count: {count}")

if __name__ == "__main__":
    main()
