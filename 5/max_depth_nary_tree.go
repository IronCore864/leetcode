package main

import "fmt"

type Node struct {
	val      int
	children []Node
}

func maxDepth(root *Node) int {
	if root == nil {
		return 0
	}
	if root.children == nil {
		return 1
	}
	res := 1
	children := root.children
	for len(children) > 0 {
		var newChildren []Node
		for _, node := range children {
			newChildren = append(newChildren, node.children...)
		}
		children = newChildren
		res++
	}
	return res
}

func main() {
	root := Node{1, []Node{
		Node{2, []Node{
			Node{3, nil},
			Node{4, nil},
		}},
		Node{5, nil},
	}}
	fmt.Println(maxDepth(&root))
}
