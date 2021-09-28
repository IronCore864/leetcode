package main

import "fmt"

func search(nums []int, target int) int {
	start, end := 0, len(nums)-1
	for start <= end {
		mid := (start + end) / 2
		switch {
		case target == nums[mid]:
			return mid
		case target < nums[mid]:
			end = mid - 1
		case target > nums[mid]:
			start = mid + 1
		}
	}
	return -1
}

func main() {
	a := []int{-1, 0, 3, 5, 9, 12}
	fmt.Println(search(a, 9))
	fmt.Println(search(a, 2))

	b := []int{1}
	fmt.Println(search(b, 1))
	fmt.Println(search(b, 2))
}
