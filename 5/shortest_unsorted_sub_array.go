package main

import (
	"fmt"
)

func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func minInt(a, b int) int {
	if a < b {
		return a
	}
	return b
}
func findUnsortedSubarray(nums []int) int {
	if nums == nil {
		return 0
	}

	n := len(nums)

	if n == 1 {
		return 0
	}

	start := -1
	end := -1

	max_from_left := nums[0]
	min_from_right := nums[n-1]

	for i := 1; i < n; i += 1 {
		max_from_left = maxInt(max_from_left, nums[i])
		min_from_right = minInt(min_from_right, nums[n-1-i])
		if nums[i] < max_from_left {
			end = i
		}
		if nums[n-1-i] > min_from_right {
			start = n - 1 - i
		}
	}
	if start == -1 {
		return 0
	}
	return end - start + 1
}

func main() {
	fmt.Println("Hello, playground")
}
