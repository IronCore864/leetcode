package main

import (
	"fmt"
	"strconv"
)

func calPoints(ops []string) int {
	stack := make([]int, 0)
	for _, s := range ops {
		switch s {
		case "+":
			if len(stack) >= 2 {
				stack = append(stack, stack[len(stack)-1]+stack[len(stack)-2])
			}
		case "D":
			stack = append(stack, stack[len(stack)-1]*2)
		case "C":
			stack = stack[:len(stack)-1]
		default:
			intVal, err := strconv.Atoi(s)
			if err == nil {
				stack = append(stack, intVal)
			} else {
				panic("str to int convertion error!")
			}
		}
	}
	sum := 0
	for _, v := range stack {
		sum += v
	}
	return sum
}

func main() {
	input := []string{"5", "2", "C", "D", "+"}
	fmt.Println(calPoints(input))
}
