package main

import "fmt"

func toLowerCase(str string) string {
	res := make([]rune, 0)
	for _, c := range str {
		if c >= 65 && c <= 90 {
			res = append(res, c+32)
		} else {
			res = append(res, c)
		}
	}
	return string(res)
}

func main() {
	fmt.Println(toLowerCase("Hello"))
}
