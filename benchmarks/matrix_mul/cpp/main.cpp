#include <iostream>
#include <vector>

const int N = 512;

void mat_mul(const std::vector<double>& a, const std::vector<double>& b, std::vector<double>& c) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            double sum = 0.0;
            for (int k = 0; k < N; ++k) {
                sum += a[i * N + k] * b[k * N + j];
            }
            c[i * N + j] = sum;
        }
    }
}

int main() {
    std::vector<double> a(N * N, 1.0);
    std::vector<double> b(N * N, 1.0);
    std::vector<double> c(N * N);

    mat_mul(a, b, c);

    std::cout << "Done. C[0][0] = " << c[0] << std::endl;
    return 0;
}
