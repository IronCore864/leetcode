package main

import (
	"fmt"
	"strings"
)

func counter(word string) map[rune]int {
	res := make(map[rune]int)
	for _, rune := range word {
		res[rune]++
	}
	return res
}

func shortestCompletingWord(licensePlate string, words []string) string {
	licenseLower := strings.ToLower(licensePlate)
	var licenseLetterOnly []rune
	for _, c := range licenseLower {
		if c >= 'a' && c <= 'z' {
			licenseLetterOnly = append(licenseLetterOnly, c)
		}
	}
	licenseCounter := counter(string(licenseLetterOnly))

	res := "abcdeabcdeabcde"
	for _, w := range words {
		wordCounter := counter(w)
		match := true
		for k, v := range licenseCounter {
			if wordCounter[k] < v {
				match = false
				break
			}
		}
		if match && len(w) < len(res) {
			res = w
		}
	}
	return res
}

func main() {
	fmt.Println(shortestCompletingWord("1s3 PSt", []string{"step", "steps", "stripe", "stepple"}))
}
