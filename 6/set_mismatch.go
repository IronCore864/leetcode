package main

import (
	"fmt"
	"sort"
)

func sum(nums []int) int {
	var sum int
	for _, v := range nums {
		sum += v
	}
	return sum
}

func findErrorNums(nums []int) []int {
	sort.Ints(nums)
	var repeating int
	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1] {
			repeating = nums[i]
			break
		}
	}
	missing := (1+len(nums))*len(nums)/2 - sum(nums) + repeating
	return []int{repeating, missing}
}

func main() {
	sli := []int{2, 3, 2}
	fmt.Println(findErrorNums(sli))
}
