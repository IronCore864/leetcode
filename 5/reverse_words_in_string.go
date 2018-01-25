package main

import (
    "fmt"
    "strings"
)

func Reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

func reverseWords(s string) string {
    words := strings.Split(s, " ")
    for i := 0; i < len(words); i += 1 {
        words[i] = Reverse(words[i])
    }
    res := strings.Join(words, " ")
    fmt.Println(res)
    return res
}

func main() {
	reverseWords("Let's take LeetCode contest")
}
