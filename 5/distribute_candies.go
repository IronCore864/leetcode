package main

import (
	"fmt"
)

func distributeCandies(candies []int) int {
	m := make(map[int]bool)
	for _, v := range candies {
		m[v] = true
	}
	s := len(m)
	l := len(candies) / 2
	if s > l {
		return l
	}
	return s
}

func main() {
	candies := []int{1, 1, 2, 2, 3, 3}
	fmt.Println(distributeCandies(candies))
}
