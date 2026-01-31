package main

import "fmt"

const N = 512

func mat_mul(a, b, c []float64) {
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			sum := 0.0
			for k := 0; k < N; k++ {
				sum += a[i*N+k] * b[k*N+j]
			}
			c[i*N+j] = sum
		}
	}
}

func main() {
	a := make([]float64, N*N)
	b := make([]float64, N*N)
	c := make([]float64, N*N)

	for i := 0; i < N*N; i++ {
		a[i] = 1.0
		b[i] = 1.0
	}

	mat_mul(a, b, c)

	fmt.Printf("Done. C[0][0] = %f\n", c[0])
}
