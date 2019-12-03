package main

import "fmt"

func isPalindrome(s []rune) bool {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			return false
		}
	}
	return true
}

func validPalindrome(s string) bool {
	runes := []rune(s)
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		if runes[i] == runes[j] {
			continue
		}
		return isPalindrome(runes[i:j]) || isPalindrome(runes[i+1:j+1])
	}
	return true
}

func main() {
	res := validPalindrome("eccer")
	fmt.Println(res)
}
