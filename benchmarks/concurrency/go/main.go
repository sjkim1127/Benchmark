package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

const N_TASKS = 100000

func main() {
	var counter int64
	var wg sync.WaitGroup

	wg.Add(N_TASKS)
	for i := 0; i < N_TASKS; i++ {
		go func() {
			atomic.AddInt64(&counter, 1)
			wg.Done()
		}()
	}

	wg.Wait()
	fmt.Printf("Done. Counter: %d\n", counter)
}
