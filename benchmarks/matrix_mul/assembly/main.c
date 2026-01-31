#include <stdio.h>
#include <stdlib.h>

extern void matmul_asm(double* A, double* B, double* C, int N);

int main() {
    int N = 512;
    double* A = (double*)malloc(N * N * sizeof(double));
    double* B = (double*)malloc(N * N * sizeof(double));
    double* C = (double*)calloc(N * N, sizeof(double));

    for (int i = 0; i < N * N; i++) {
        A[i] = 1.0;
        B[i] = 1.0;
    }

    matmul_asm(A, B, C, N);

    // Verify a few elements
    if (C[0] == (double)N && C[N*N-1] == (double)N) {
        printf("Done\n");
    } else {
        printf("Verification failed: %f\n", C[0]);
    }

    free(A);
    free(B);
    free(C);
    return 0;
}
