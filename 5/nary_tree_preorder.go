package main

import (
	"fmt"
)

type Node struct {
	val      int
	children []*Node
}

func preorder(root *Node) []int {
	if root == nil {
		return make([]int, 0)
	}
	stack := []*Node{root}
	var res []int
	for len(stack) > 0 {
		current := stack[len(stack)-1]
		stack = stack[0 : len(stack)-1]
		res = append(res, current.val)
		for i := len(current.children) - 1; i >= 0; i-- {
			stack = append(stack, current.children[i])
		}
	}
	return res
}

func main() {
	n21 := Node{2, make([]*Node, 0)}
	n22 := Node{4, make([]*Node, 0)}
	n11 := Node{3, []*Node{&n21, &n22}}
	n12 := Node{5, make([]*Node, 0)}
	n13 := Node{6, make([]*Node, 0)}
	root := Node{1, []*Node{&n11, &n12, &n13}}
	fmt.Println(preorder(&root))
}
