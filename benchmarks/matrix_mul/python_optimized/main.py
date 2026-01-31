
import numpy as np
import time

N = 512

def main():
    a = np.ones((N, N), dtype=np.float64)
    b = np.ones((N, N), dtype=np.float64)

    # Note: Measuring just the operation, like other benchmarks
    start = time.time()
    c = np.dot(a, b)
    end = time.time()

    if c[0, 0] == float(N):
        print("Done")
    else:
        print("Fail")

if __name__ == "__main__":
    main()
