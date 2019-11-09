package main

import (
	"fmt"
)

func fib(N int) int {
	if N == 0 {
		return 0
	}

	if N == 1 {
		return 1
	}

	a := 0
	b := 0
	res := 1

	for i := 2; i <= N; i++ {
		a = b
		b = res
		res = a + b
	}

	return res
}

func main() {
	for i := 0; i < 10; i++ {
		fmt.Println(fib(i))
	}
}
