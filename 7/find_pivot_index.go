package main

import "fmt"

func sum(nums []int) int {
	res := 0
	for i := 0; i < len(nums); i++ {
		res += nums[i]
	}
	return res
}

func pivotIndex(nums []int) int {
	leftSum := 0
	rightSum := sum(nums)
	for i := 0; i < len(nums); i++ {
		rightSum -= nums[i]
		if leftSum == rightSum {
			return i
		}
		leftSum += nums[i]
	}
	return -1
}

func main() {
	nums := []int{1, 7, 3, 6, 5, 6}
	fmt.Println(pivotIndex(nums))
}
