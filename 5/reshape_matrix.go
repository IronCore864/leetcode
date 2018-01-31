package main

import (
	"fmt"
)

func matrixReshape(nums [][]int, r int, c int) [][]int {
	if nums == nil {
		return nums
	}

	if nums[0] == nil {
		return nums
	}

	row := len(nums)
	col := len(nums[0])

	if row*col != c*r {
		return nums
	}

	res := make([][]int, r)

	for i := range res {
		res[i] = make([]int, c)
	}

	for i := 0; i < r; i += 1 {
		for j := 0; j < c; j += 1 {
			orig_i := (i*c + j) / col
			orig_j := (i*c + j) % col
			res[i][j] = nums[orig_i][orig_j]
		}
	}

	return res
}

func main() {
	a := [][]int{
		{0, 1, 2, 3},
		{4, 5, 6, 7},
	}

	fmt.Println(matrixReshape(a, 4, 2))
}
