package main

import "fmt"

type Node struct {
	Left, Right *Node
}

func createTree(depth int) *Node {
	if depth == 0 {
		return nil
	}
	return &Node{
		Left:  createTree(depth - 1),
		Right: createTree(depth - 1),
	}
}

func main() {
	depth := 20
	root := createTree(depth)
	if root != nil {
		fmt.Printf("Tree allocated. Depth: %d\n", depth)
	}
}
