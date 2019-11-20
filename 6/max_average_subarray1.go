package main

import "fmt"

func sum(nums []int) int {
	var sum int
	for _, v := range nums {
		sum += v
	}
	return sum
}

func findMaxAverage(nums []int, k int) float64 {
	preSum := sum(nums[0:k])
	maxSum := preSum
	var nextSum int
	for i := 0; i < len(nums)-k; i++ {
		nextSum = preSum - nums[i] + nums[i+k]
		if nextSum > maxSum {
			maxSum = nextSum
		}
		preSum = nextSum
	}
	return float64(maxSum) / float64(k)
}

func main() {
	sli := []int{1, 12, -5, -6, 50, 3}
	fmt.Println(findMaxAverage(sli, 4))
}
