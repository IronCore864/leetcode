package main

import (
	"fmt"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func findShortestSubArray(nums []int) int {
	first, count, res, degree := make(map[int]int), make(map[int]int), 0, 0

	for i, num := range nums {
		if val, ok := first[num]; ok {
			first[num] = min(val, i)
		} else {
			first[num] = i
		}

		count[num]++

		if count[num] > degree {
			degree = count[num]
			res = i - first[num] + 1
		} else if count[num] == degree {
			res = min(res, i-first[num]+1)
		}

	}

	return res
}

func main() {
	fmt.Println(findShortestSubArray([]int{1, 2, 2, 3, 1}))
	fmt.Println(findShortestSubArray([]int{1, 2, 2, 3, 1, 4, 2}))
}
