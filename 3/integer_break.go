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

func integerBreak(n int) int {
	dp := []int{0, 1}
	for i := 2; i <= n; i++ {
		a := 1
		b := i - a
		maxProduct := 0
		for a <= b {
			maxProduct = maxInt(maxProduct, maxInt(a, dp[a])*maxInt(b, dp[b]))
			a++
			b--
		}
		dp = append(dp, maxProduct)

	}
	return dp[len(dp)-1]
}

func main() {
	fmt.Println(integerBreak(3))
	fmt.Println(integerBreak(8))
	fmt.Println(integerBreak(58))
}

