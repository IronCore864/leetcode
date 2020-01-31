package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func min(a, b int) int {
	if a <= b {
		return a
	}
	return b
}

func inOrder(root *TreeNode, previousVal, result *int) {
	if root.Left != nil {
		inOrder(root.Left, previousVal, result)
	}
	*result = min(*result, root.Val-*previousVal)
	*previousVal = root.Val
	if root.Right != nil {
		inOrder(root.Right, previousVal, result)
	}
}

func minDiffInBST(root *TreeNode) int {
	previousVal := -2147483647
	result := 2147483647
	inOrder(root, &previousVal, &result)
	return result
}

func main() {
	root := TreeNode{4, &TreeNode{2, &TreeNode{1, nil, nil}, &TreeNode{3, nil, nil}}, &TreeNode{6, nil, nil}}
	fmt.Println(minDiffInBST(&root))
}
