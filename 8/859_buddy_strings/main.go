package main

import "fmt"

func buddyStrings(a string, b string) bool {
	if len(a) != len(b) || len(a) == 1 {
		return false
	}

	p0, p1 := -1, -1
	duplicatedLetters := false
	count := [26]bool{}

	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			if p0 == -1 {
				p0 = i
			} else if p1 == -1 {
				p1 = i
			} else {
				return false
			}
		}
		if count[a[i]-'a'] == true {
			duplicatedLetters = true
		}
		count[a[i]-'a'] = true
	}

	if p0 == -1 {
		return duplicatedLetters
	}
	if p1 == -1 {
		return false
	}
	return a[p0] == b[p1] && a[p1] == b[p0]
}

func main() {
	fmt.Println(buddyStrings("abcd", "cbad"))
	fmt.Println(buddyStrings("ab", "ba"))
	fmt.Println(buddyStrings("ab", "ab"))
	fmt.Println(buddyStrings("aa", "aa"))
	fmt.Println(buddyStrings("ab", "ba"))
	fmt.Println(buddyStrings("aaaaaaabc", "aaaaaaacb"))
}
