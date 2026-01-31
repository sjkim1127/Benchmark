#include <stdio.h>

// Declare the external assembly function
extern long long fib_asm(long long n);

int main() {
    long long n = 40;
    long long result = fib_asm(n);
    printf("Result: %lld\n", result);
    return 0;
}
