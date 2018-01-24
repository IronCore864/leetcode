package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func depth(root *TreeNode, maxlen *int) int {
	if root == nil {
		return 0
	}
	var l = depth(root.Left, maxlen)
	var r = depth(root.Right, maxlen)
	*maxlen = Max(l+r+1, *maxlen)
	return Max(l, r) + 1
}

func diameterOfBinaryTree(root *TreeNode) int {
	var maxlen = 0
	if root == nil {
		return 0
	}
	depth(root, &maxlen)
	fmt.Println(maxlen - 1)
	return maxlen - 1
}

func main() {
	var root = TreeNode{1, nil, nil}
	diameterOfBinaryTree(&root)
}
