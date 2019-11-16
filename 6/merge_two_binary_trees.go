package main

import "fmt"

// TreeNode is the struct for tree node
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func mergeTrees(t1 *TreeNode, t2 *TreeNode) *TreeNode {
	if *t1 == (TreeNode{}) {
		return t2
	}
	if *t2 == (TreeNode{}) {
		return t1
	}
	stack := [][]*TreeNode{[]*TreeNode{t1, t2}}
	for len(stack) > 0 {
		n1 := stack[len(stack)-1][0]
		n2 := stack[len(stack)-1][1]
		stack = stack[0 : len(stack)-1]
		if *n1 == (TreeNode{}) || *n2 == (TreeNode{}) {
			continue
		}
		n1.Val += n2.Val
		if *(n1.Left) == (TreeNode{}) {
			n1.Left = n2.Left
		} else {
			stack = append(stack, []*TreeNode{n1.Left, n2.Left})
		}
		if *(n1.Right) == (TreeNode{}) {
			n1.Right = n2.Right
		} else {
			stack = append(stack, []*TreeNode{n1.Right, n2.Right})
		}
	}
	return t1
}

func printTree(root *TreeNode) {
	q := []*TreeNode{root}
	res := make([]int, 0)
	for len(q) > 0 {
		newQ := make([]*TreeNode, 0)
		for _, node := range q {
			res = append(res, node.Val)
			if *(node.Left) != (TreeNode{}) {
				newQ = append(newQ, node.Left)
			}
			if *(node.Right) != (TreeNode{}) {
				newQ = append(newQ, node.Right)
			}
		}
		q = newQ
	}
	fmt.Println(res)
}

func main() {
	t1 := TreeNode{1, &TreeNode{3, &TreeNode{5, &TreeNode{}, &TreeNode{}}, &TreeNode{}}, &TreeNode{2, &TreeNode{}, &TreeNode{}}}
	t2 := TreeNode{2, &TreeNode{1, &TreeNode{}, &TreeNode{4, &TreeNode{}, &TreeNode{}}}, &TreeNode{3, &TreeNode{}, &TreeNode{7, &TreeNode{}, &TreeNode{}}}}
	printTree(&t1)
	printTree(&t2)
	printTree(mergeTrees(&t1, &t2))
}
