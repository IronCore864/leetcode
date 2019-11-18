package main

import (
	"fmt"
	"math"
)

func float64IsInt(f float64) bool {
	return f == float64(int(f))
}

func judgeSquareSum(c int) bool {
	for a := 0; a <= int(math.Sqrt(float64(c/2))); a++ {
		b := math.Sqrt(float64(c - a*a))
		if float64IsInt(b) {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println(judgeSquareSum(5))
	fmt.Println(judgeSquareSum(6))
}
