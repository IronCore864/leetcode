package main

import (
	"fmt"
)

func minInt(m, n int) int {
	if m < n {
		return m
	}
	return n

}

func maxCount(m int, n int, ops [][]int) int {
    if len(ops) == 0 {
		return m * n
	}

	i, j := 40000, 40000

	for _, op := range ops {
		i, j = minInt(i, op[0]), minInt(j, op[1])
	}
	return i * j

}

func main() {
	ops := [][]int{
		{2, 2},
		{3, 3},
	}
	res := maxCount(3, 3, ops)
	fmt.Println(res)
}
