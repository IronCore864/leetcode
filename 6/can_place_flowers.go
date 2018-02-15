package main

import (
	"fmt"
)

func canPlace(flowerbed []int, i int) bool {
	if flowerbed[i] == 1 {
		return false
	}

	if i-1 >= 0 && i+1 < len(flowerbed) {
		if flowerbed[i-1] == 0 && flowerbed[i+1] == 0 {
			flowerbed[i] = 1
			return true
		} else {
			return false
		}
	}

	if i-1 < 0 && i+1 >= len(flowerbed) {
		return true
	}

	if i-1 < 0 {
		if flowerbed[i+1] == 0 {
			flowerbed[i] = 1
			return true
		}
	}

	if i+1 >= len(flowerbed) {
		if flowerbed[i-1] == 0 {
			flowerbed[i] = 1
			return true
		}
	}
	return false
}

func canPlaceFlowers(flowerbed []int, n int) bool {
	c := 0
	for i := 0; i < len(flowerbed); i += 1 {
		if canPlace(flowerbed, i) {
			c += 1
		}
	}
	return n <= c
}

func main() {
	f := []int{0}
	fmt.Println(canPlaceFlowers(f, 1))
	f = []int{1}
	fmt.Println(canPlaceFlowers(f, 0))
}
