package main

import (
	"fmt"
	"strings"
)

func multiplyString(s string, times int) string {
	res := ""
	for i := 0; i < times; i++ {
		res += s
	}
	return res
}

func repeatedStringMatch(A string, B string) int {
	for _, rune := range B {
		if strings.Index(A, string(rune)) == -1 {
			return -1
		}
	}
	res := len(B) / len(A)
	if strings.Index(multiplyString(A, res), B) != -1 {
		return res
	} else if strings.Index(multiplyString(A, res+1), B) != -1 {
		return res + 1
	} else if strings.Index(multiplyString(A, res+2), B) != -1 {
		return res + 2
	} else {
		return -1
	}
}

func main() {
	a := "abcd"
	b := "cdabcdab"
	fmt.Println(repeatedStringMatch(a, b))
}
