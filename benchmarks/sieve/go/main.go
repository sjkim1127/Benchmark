package main

import (
	"fmt"
	"math"
)

const LIMIT = 10000000

func runSieve() int {
	// Go slices are efficient
	isPrime := make([]bool, LIMIT+1)
	
	// Initialize
	for i := 0; i <= LIMIT; i++ {
		isPrime[i] = true
	}
	isPrime[0] = false
	isPrime[1] = false

	// Sieve
	sqrtLimit := int(math.Sqrt(float64(LIMIT)))
	for p := 2; p <= sqrtLimit; p++ {
		if isPrime[p] {
			for i := p * p; i <= LIMIT; i += p {
				isPrime[i] = false
			}
		}
	}

	count := 0
	for p := 2; p <= LIMIT; p++ {
		if isPrime[p] {
			count++
		}
	}

	return count
}

func main() {
	count := runSieve()
	fmt.Printf("Count: %d\n", count)
}
