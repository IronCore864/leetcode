package main

import (
	"fmt"
)

func maxInt(a, b, c int) int {
	switch {
	case a >= b && a >= c:
		return a
	case b >= a && b >= c:
		return b
	}
	return c
}

func findLHS(nums []int) int {
	counter := make(map[int]int)
	for _, num := range nums {
		counter[num] += 1
	}

	res := 0

	for k, v := range counter {
		if counter[k-1] == 0 && counter[k+1] == 0 {
			continue
		}
		res = maxInt(res, v+counter[k-1], v+counter[k+1])
	}

	return res
}

func main() {
	arr := []int{1, 3, 2, 2, 5, 2, 3, 7}
	fmt.Println(findLHS(arr))
}
