package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSame(s, t *TreeNode) bool {
	switch {
	case s == nil && t == nil:
		return true
	case s == nil:
		return false
	case t == nil:
		return false
	default:
		return s.Val == t.Val && isSame(s.Left, t.Left) && isSame(s.Right, t.Right)
	}
}

func isSubtree(s *TreeNode, t *TreeNode) bool {
	if s == nil || t == nil {
		return false
	}

	return isSame(s, t) || isSubtree(s.Left, t) || isSubtree(s.Right, t)
}

func main() {
	fmt.Println("Hello, playground")
}
