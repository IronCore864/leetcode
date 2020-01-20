package main

import (
	"fmt"
	"strconv"
)

func contains(arr []int, num int) bool {
	for i := 0; i < len(arr); i++ {
		if arr[i] == num {
			return true
		}
	}
	return false
}

func isPrime(num int) bool {
	if contains([]int{2, 3, 5, 7, 11, 13, 17, 19}, num) {
		return true
	}
	return false
}

func countPrimeSetBits(L int, R int) int {
	res := 0
	for num := L; num <= R; num++ {
		bin := strconv.FormatInt(int64(num), 2)

		count := 0
		for _, rune := range bin {
			if rune == '1' {
				count++
			}
		}

		if isPrime(count) {
			res++
		}
	}
	return res
}

func main() {
	fmt.Println(countPrimeSetBits(6, 10))
}
