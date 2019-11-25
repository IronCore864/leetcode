package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findTarget(root *TreeNode, k int) bool {
	s := map[int]bool{}

	if root == nil {
		return false
	}

	currentRow := []*TreeNode{root}
	for len(currentRow) > 0 {
		nextRow := []*TreeNode{}

		for _, node := range currentRow {
			_, ok := s[k-node.Val]
			if ok {
				return true
			}
			s[node.Val] = true
			if node.Left != nil {
				nextRow = append(nextRow, node.Left)
			}
			if node.Right != nil {
				nextRow = append(nextRow, node.Right)
			}
		}
		currentRow = nextRow
	}
	return false
}

func main() {
	root := TreeNode{5,
		&TreeNode{3, &TreeNode{2, nil, nil}, &TreeNode{4, nil, nil}},
		&TreeNode{6, nil, &TreeNode{7, nil, nil}}}
	fmt.Println(findTarget(&root, 9))
	fmt.Println(findTarget(&root, 27))
}
