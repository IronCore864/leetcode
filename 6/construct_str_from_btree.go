package main

import (
	"fmt"
)

type Node struct {
	val   int
	left  *Node
	right *Node
}

func tree2str(n *Node) string {
	if n == nil {
		return ""
	}

	if n.left == nil && n.right == nil {
		return fmt.Sprintf("%d", n.val)
	} else if n.left == nil {
		return fmt.Sprintf("%d()(%s)", n.val, tree2str(n.right))

	} else if n.right == nil {
		return fmt.Sprintf("%d(%s)", n.val, tree2str(n.left))
	} else {
		return fmt.Sprintf("%d(%s)(%s)", n.val, tree2str(n.left), tree2str(n.right))
	}
}

func main() {
	n21 := Node{4, nil, nil}
	n11 := Node{2, &n21, nil}
	n12 := Node{3, nil, nil}
	root := Node{1, &n11, &n12}
	fmt.Println(tree2str(&root))
}
