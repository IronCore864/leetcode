package main

import (
	"fmt"
)

type Node struct {
	val      int
	children []*Node
}

func reverseSli(a []int) []int {
	for i := len(a)/2 - 1; i >= 0; i-- {
		opp := len(a) - 1 - i
		a[i], a[opp] = a[opp], a[i]
	}
	return a
}

func postorder(root *Node) []int {
	if root == nil {
		return make([]int, 0)
	}

	stack := []*Node{root}
	var res []int
	for len(stack) > 0 {
		current := stack[len(stack)-1]
		stack = stack[0 : len(stack)-1]
		res = append(res, current.val)
		for i := 0; i < len(current.children); i++ {
			stack = append(stack, current.children[i])
		}
	}
	return reverseSli(res)
}

func main() {
	n21 := Node{5, make([]*Node, 0)}
	n22 := Node{6, make([]*Node, 0)}
	n11 := Node{2, []*Node{&n21, &n22}}
	n12 := Node{3, make([]*Node, 0)}
	n13 := Node{4, make([]*Node, 0)}
	root := Node{1, []*Node{&n11, &n12, &n13}}
	fmt.Println(postorder(&root))
}
