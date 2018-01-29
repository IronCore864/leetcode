package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sum(root *TreeNode, total_tilt *int) int {
	if root == nil {
		return 0
	}
	sum_left := sum(root.Left, total_tilt)
	sum_right := sum(root.Right, total_tilt)
	tilt := sum_left - sum_right
	if tilt < 0 {
		tilt = -tilt
	}
	*total_tilt += tilt
	return sum_left + sum_right + root.Val
}

func findTilt(root *TreeNode) int {
	var ans int = 0
	sum(root, &ans)
	return ans
}

func main() {
	fmt.Println("Hello, playground")
}
