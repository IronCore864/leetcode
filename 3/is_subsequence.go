package main

import (
	"fmt"
	"strings"
)

func isSubsequence(s string, t string) bool {
	if s == "" {
		return true
	}

	for _, c := range s {
		pos := strings.IndexRune(t, c)
		if pos == -1 {
			return false
		}
		t = t[pos+1:]
	}
	return true
}

func main() {
	fmt.Println(isSubsequence("abc", "ahbgdc"))
}
