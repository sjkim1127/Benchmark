package main

import "fmt"

func fib(n int) int64 {
	if n <= 1 {
		return int64(n)
	}
	return fib(n-1) + fib(n-2)
}

func main() {
	result := fib(40)
	fmt.Printf("Result: %d\n", result)
}
