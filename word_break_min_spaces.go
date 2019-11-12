package main

import (
	"fmt"
	"math"
)

func keyInMap(key string, m *map[string]int) bool {
	if _, ok := (*m)[key]; ok {
		return true
	}
	return false
}

func minInt(a, b int) int {
	fA := float64(a)
	fB := float64(b)
	min := math.Min(fA, fB)
	return int(min)
}

func minSpaceBreak(str string, fav []string) int {
	m := make(map[string]int)
	for _, s := range fav {
		m[s] = 0
	}

	dp := make([]int, len(str))
	for i := 0; i < len(str); i++ {
		if keyInMap(str[0:i+1], &m) {
			dp[i] = 0
		} else {
			numOfSpaces := math.MaxInt64
			for k := 0; k < i; k++ {
				if dp[k] != math.MaxInt64 && keyInMap(str[k+1:i+1], &m) {
					numOfSpaces = minInt(numOfSpaces, dp[k]+1)
				}
			}
			dp[i] = numOfSpaces
		}
	}
	return dp[len(str)-1]
}

func main() {
	str := "31415926"
	fav := []string{"314", "31415", "15", "926"}
	fmt.Println(minSpaceBreak(str, fav))
}
