package main

import (
	"fmt"
)

func findRestaurant(list1 []string, list2 []string) []string {
	m := make(map[string]int)

	for i, s := range list1 {
		m[s] = i
	}

	var res []string
	i := 2000

	for i2, s := range list2 {
		if i1, ok := m[s]; ok {
			if i1+i2 == i {
				res = append(res, s)
			}
			if i1+i2 < i {
				i = i1 + i2
				res = []string{s}
			}
		}
	}
	return res
}

func main() {
	fmt.Println("Hello, playground")
}
