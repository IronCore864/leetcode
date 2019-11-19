package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func averageOfLevels(root *TreeNode) []float64 {
	if root == nil {
		return make([]float64, 0)
	}

	res := make([]float64, 0)
	row := []*TreeNode{root}
	for len(row) > 0 {
		nextRow := make([]*TreeNode, 0)
		var sum float64
		for _, n := range row {
			sum += float64(n.Val)
			if n.Left != nil {
				nextRow = append(nextRow, n.Left)
			}
			if n.Right != nil {
				nextRow = append(nextRow, n.Right)
			}
		}
		res = append(res, sum/float64(len(row)))
		row = nextRow
	}
	return res
}

func main() {
	r := TreeNode{3,
		&TreeNode{9, nil, nil},
		&TreeNode{20,
			&TreeNode{15, nil, nil},
			&TreeNode{7, nil, nil}}}
	fmt.Println(averageOfLevels(&r))
}
