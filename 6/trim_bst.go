package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func trimBST(root *TreeNode, L int, R int) *TreeNode {
	if root == nil {
		return nil
	}

	if root.Left == nil && root.Right == nil {
		if root.Val < L || root.Val > R {
			return nil
		}
		return root
	}

	if root.Val < L {
		return trimBST(root.Right, L, R)
	}

	if root.Val > R {
		return trimBST(root.Left, L, R)
	}

	root.Left = trimBST(root.Left, L, R)
	root.Right = trimBST(root.Right, L, R)
	return root
}

func main() {
	root := TreeNode{3,
		&TreeNode{0,
			nil,
			&TreeNode{2,
				&TreeNode{1, nil, nil},
				nil}},
		&TreeNode{4, nil, nil}}

	res := trimBST(&root, 1, 3)
	fmt.Println(res)
	fmt.Println(res.Left)
	fmt.Println(res.Right)
	fmt.Println(res.Left.Left)
}
