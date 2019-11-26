package main

import (
	"fmt"
)

func judgeCircle(moves string) bool {
	var l, r, u, d int
	for _, c := range moves {
		switch c {
		case 'L':
			l++
		case 'R':
			r++
		case 'U':
			u++
		case 'D':
			d++
		}
	}
	return l == r && u == d
}

func main() {
	fmt.Println(judgeCircle("LLRR"))
	fmt.Println(judgeCircle("LLR"))
}
