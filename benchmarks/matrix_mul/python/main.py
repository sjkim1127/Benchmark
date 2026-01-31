import sys

# Increase N for Python? No, 512^3 is 134M operations. 
# Pure Python might take too long (minutes). 
# Let's keep 512 but be aware it's slow. 
# Or reduce N for all languages if Python is too slow?
# C runs 512 in ~0.2s. Python is 100x slower -> 20s. 20s is acceptable.
N = 512

def mat_mul(A, B):
    C = [[0.0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            total = 0.0
            for k in range(N):
                total += A[i][k] * B[k][j]
            C[i][j] = total
    return C

def main():
    A = [[1.0] * N for _ in range(N)]
    B = [[1.0] * N for _ in range(N)]
    
    C = mat_mul(A, B)
    
    print(f"Done. C[0][0] = {C[0][0]}")

if __name__ == "__main__":
    main()
