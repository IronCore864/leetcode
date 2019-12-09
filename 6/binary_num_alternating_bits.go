package main

import (
	"fmt"
	"math"
)

func pow(a, b int) int {
	return int(math.Pow(float64(a), float64(b)))
}

func hasAlternatingBits(n int) bool {
	res := 0
	var i int
	if n%2 == 0 {
		i = 1
	}

	for res < n {
		res += pow(2, i)
		i += 2
	}
	if res == n {
		return true
	}
	return false
}

func main() {
	fmt.Println(hasAlternatingBits(5))
	fmt.Println(hasAlternatingBits(7))
	fmt.Println(hasAlternatingBits(10))
	fmt.Println(hasAlternatingBits(11))
}
