#include <stdio.h>
#include <stdlib.h>

// naive recursive fibonacci
long long fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}

int main() {
    int n = 40;
    long long result = fib(n);
    printf("Result: %lld\n", result);
    return 0;
}
