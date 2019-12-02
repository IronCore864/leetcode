package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b

}

func findLengthOfLCIS(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	maxLen := 1
	currentLen := 1

	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[i-1] {
			currentLen++
		} else {
			maxLen = max(maxLen, currentLen)
			currentLen = 1
		}
	}

	maxLen = max(maxLen, currentLen)
	return maxLen
}

func main() {
	res := findLengthOfLCIS([]int{3, 4, 5, 2, 3})
	fmt.Println(res)
}
