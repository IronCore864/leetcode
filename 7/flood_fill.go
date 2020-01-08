package main

import "fmt"

func fill(row, col int, image [][]int, color, newColor int) {
	if !(0 <= row && row < len(image) && 0 <= col && col < len(image[0])) || image[row][col] != color {
		return
	}
	image[row][col] = newColor
	fill(row-1, col, image, color, newColor)
	fill(row+1, col, image, color, newColor)
	fill(row, col-1, image, color, newColor)
	fill(row, col+1, image, color, newColor)
}

func floodFill(image [][]int, sr int, sc int, newColor int) [][]int {
	if image[sr][sc] != newColor {
		fill(sr, sc, image, image[sr][sc], newColor)
	}
	return image
}

func main() {
	image := [][]int{
		[]int{1, 1, 1},
		[]int{1, 1, 0},
		[]int{1, 0, 1},
	}

	fmt.Println(floodFill(image, 1, 1, 2))
}
