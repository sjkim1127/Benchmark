#include <iostream>
#include <vector>
#include <complex>

const int WIDTH = 2048;
const int HEIGHT = 2048;
const int MAX_ITER = 255;

int main() {
    std::vector<unsigned char> buffer(WIDTH * HEIGHT);

    double min_x = -2.0;
    double max_x = 0.47;
    double min_y = -1.12;
    double max_y = 1.12;
    
    double scalex = (max_x - min_x) / WIDTH;
    double scaley = (max_y - min_y) / HEIGHT;

    for (int y = 0; y < HEIGHT; y++) {
        double cy = min_y + y * scaley;
        for (int x = 0; x < WIDTH; x++) {
            double cx = min_x + x * scalex;
            
            // std::complex might be slightly slower than manual doubles?
            // Let's stick to manual doubles to be consistent with C and maximize perf.
            double zx = 0.0;
            double zy = 0.0;
            double zx2 = 0.0;
            double zy2 = 0.0;
            
            int iter = 0;
            while (iter < MAX_ITER && (zx2 + zy2) < 4.0) {
                zy = 2.0 * zx * zy + cy;
                zx = zx2 - zy2 + cx;
                zx2 = zx * zx;
                zy2 = zy * zy;
                iter++;
            }
            buffer[y * WIDTH + x] = iter;
        }
    }

    unsigned long sum = 0;
    for (unsigned char val : buffer) {
        sum += val;
    }
    std::cout << "Done. Sum: " << sum << std::endl;

    return 0;
}
