package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func secondMinNotEqualToVal(node *TreeNode, val int) int {
	if node.Left == nil {
		if node.Val == val {
			return -1
		} else {
			return node.Val
		}
	}
	secondMinLeft := secondMinNotEqualToVal(node.Left, val)
	secondMinRight := secondMinNotEqualToVal(node.Right, val)
	if secondMinLeft == -1 && secondMinRight == -1 {
		return -1
	} else if secondMinLeft == -1 {
		return secondMinRight
	} else if secondMinRight == -1 {
		return secondMinLeft
	} else {
		return min(secondMinLeft, secondMinRight)
	}
}

func findSecondMinimumValue(root *TreeNode) int {
	res := secondMinNotEqualToVal(root, root.Val)
	return res
}

func main() {
	root := TreeNode{2,
		&TreeNode{2, nil, nil},
		&TreeNode{5,
			&TreeNode{5, nil, nil},
			&TreeNode{7, nil, nil}}}

	res := findSecondMinimumValue(&root)
	fmt.Println(res)
}
