#include <stdio.h>
#include <stdlib.h>

#define N 512

void mat_mul(double *a, double *b, double *c) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            double sum = 0.0;
            for (int k = 0; k < N; k++) {
                sum += a[i * N + k] * b[k * N + j];
            }
            c[i * N + j] = sum;
        }
    }
}

int main() {
    double *a = (double *)malloc(N * N * sizeof(double));
    double *b = (double *)malloc(N * N * sizeof(double));
    double *c = (double *)malloc(N * N * sizeof(double));

    // Initialize
    for (int i = 0; i < N * N; i++) {
        a[i] = 1.0;
        b[i] = 1.0;
    }

    mat_mul(a, b, c);

    printf("Done. C[0][0] = %f\n", c[0]);

    free(a);
    free(b);
    free(c);
    return 0;
}
