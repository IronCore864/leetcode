package main

import "fmt"

func get(i, j int, m [][]int) (int, int) {
	if i < 0 || j < 0 || i >= len(m) || j >= len(m[0]) {
		return 0, 0
	}
	return m[i][j], 1
}

func avg(i, j int, m [][]int) int {
	var neighbourSum, neighbourCount int
	for r := i - 1; r <= i+1; r++ {
		for c := j - 1; c <= j+1; c++ {
			value, count := get(r, c, m)
			neighbourSum += value
			neighbourCount += count
		}
	}
	return neighbourSum / neighbourCount
}

func imageSmoother(m [][]int) [][]int {
	res := make([][]int, len(m))
	for i := range m {
		res[i] = make([]int, len(m[0]))
	}
	for i := 0; i < len(m); i++ {
		for j := 0; j < len(m[0]); j++ {
			res[i][j] = avg(i, j, m)
		}
	}
	return res
}

func main() {
	sli := [][]int{
		[]int{2, 3, 4},
		[]int{5, 6, 7},
		[]int{8, 9, 10},
		[]int{11, 12, 13},
		[]int{14, 15, 16},
	}
	fmt.Println(imageSmoother(sli))
}
