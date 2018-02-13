package main

import (
	"fmt"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func calculate(nums []int, dp [][]int, i int, j int) int {
	if dp[i][j] != 0 || j == i+1 {
		return dp[i][j]
	}

	coins := 0
	for k := i + 1; k < j; k += 1 {
		coins = max(coins, nums[i]*nums[k]*nums[j]+calculate(nums, dp, i, k)+calculate(nums, dp, k, j))
	}
	dp[i][j] = coins
	return coins
}

func maxCoins(nums []int) int {
	nums = append([]int{1}, nums...)
	nums = append(nums, 1)

	n := len(nums)

	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
	}

	return calculate(nums, dp, 0, n-1)
}

func main() {
	var nums = []int{3, 1, 5, 8}
	fmt.Println(maxCoins(nums))
}
