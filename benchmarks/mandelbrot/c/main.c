#include <stdio.h>
#include <stdlib.h>

#define WIDTH 2048
#define HEIGHT 2048
#define MAX_ITER 255

int main() {
    // Allocate buffer
    unsigned char *buffer = (unsigned char *)malloc(WIDTH * HEIGHT);
    
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
    
    // Prevent compiler from optimizing away the work by using the result
    // Simple checksum
    unsigned long sum = 0;
    for (int i = 0; i < WIDTH * HEIGHT; i++) {
        sum += buffer[i];
    }
    
    printf("Done. Sum: %lu\n", sum);
    free(buffer);
    return 0;
}
