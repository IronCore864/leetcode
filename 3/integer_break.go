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

// O(1) solution without proof
// https://leetcode.com/problems/integer-break/discuss/423970/O(1)-Solution
func test(n int) int {
	if n == 2 {
		return 1
	}
	if n == 3 {
		return 2
	}
	a := n / 3
	b := n % 3
	res := 1
	switch b {
	case 0:
		res = int(math.Pow(3, float64(a)))
	case 1:
		res = int(math.Pow(3, float64(a-1))) * 4
	case 2:
		res = int(math.Pow(3, float64(a))) * 2
	}
	return res
}


func main() {
	fmt.Println(integerBreak(3))
	fmt.Println(integerBreak(8))
	fmt.Println(test(8))
	fmt.Println(integerBreak(58))
	fmt.Println(test(58))
}

