import math
import time

LIMIT = 10000000

def run_sieve():
    # Python lists are dynamic arrays
    is_prime = [True] * (LIMIT + 1)
    is_prime[0] = False
    is_prime[1] = False

    sqrt_limit = int(math.isqrt(LIMIT))
    for p in range(2, sqrt_limit + 1):
        if is_prime[p]:
            # Slice assignment might be faster in Python
            # is_prime[p*p : LIMIT+1 : p] = [False] * len(...) 
            # but let's stick to the loop for comparable logic or use slice if it's "pythonic"
            # Using slice assignment is the idiomatic high-performance way in pure Python
            is_prime[p*p : LIMIT+1 : p] = [False] * ((LIMIT - p*p) // p + 1)

            # Manual loop version (slower but more comparable to C?):
            # for i in range(p*p, LIMIT + 1, p):
            #     is_prime[i] = False
            
    return sum(is_prime)

if __name__ == "__main__":
    count = run_sieve()
    print(f"Count: {count}")
