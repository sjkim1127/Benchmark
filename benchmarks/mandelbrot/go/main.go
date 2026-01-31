package main

import (
	"fmt"
)

const (
	WIDTH    = 2048
	HEIGHT   = 2048
	MAX_ITER = 255
)

func main() {
	buffer := make([]byte, WIDTH*HEIGHT)

	minX := -2.0
	maxX := 0.47
	minY := -1.12
	maxY := 1.12

	scaleX := (maxX - minX) / float64(WIDTH)
	scaleY := (maxY - minY) / float64(HEIGHT)

	for y := 0; y < HEIGHT; y++ {
		cy := minY + float64(y)*scaleY
		for x := 0; x < WIDTH; x++ {
			cx := minX + float64(x)*scaleX

			var zx, zy, zx2, zy2 float64
			iter := 0
			// In Go, complex128 might be cleaner, but let's match C logic for perf fairness
			// complex128 is usually well optimized though.
			// Let's stick to manual float64 to escape complex overhead if any.
			for iter < MAX_ITER && (zx2+zy2) < 4.0 {
				zy = 2.0*zx*zy + cy
				zx = zx2 - zy2 + cx
				zx2 = zx * zx
				zy2 = zy * zy
				iter++
			}
			buffer[y*WIDTH+x] = byte(iter)
		}
	}

	var sum uint64
	for _, b := range buffer {
		sum += uint64(b)
	}

	fmt.Printf("Done. Sum: %d\n", sum)
}
