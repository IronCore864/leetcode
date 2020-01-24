package main

import (
	"fmt"
)

func isToeplitzMatrix(matrix [][]int) bool {
	r, c := len(matrix), len(matrix[0])

	for i := 0; i < r; i++ {
		curI, curJ := i, 0
		for curI < r && curJ < c {
			if matrix[curI][curJ] != matrix[i][0] {
				return false
			}
			curI++
			curJ++
		}
	}

	for j := 0; j < c; j++ {
		curI, curJ := 0, j
		for curI < r && curJ < c {
			if matrix[curI][curJ] != matrix[0][j] {
				return false
			}
			curI++
			curJ++
		}
	}

	return true
}

func main() {
	fmt.Println(isToeplitzMatrix([][]int{[]int{1, 2, 3, 4}, []int{5, 1, 2, 3}, []int{9, 5, 1, 2}}))
}
