package main

import "fmt"

func checkRecord(s string) bool {
	absent := 0
	continuous_late := 0

	runes := []rune(s)
	for i := 0; i < len(runes); i++ {
		switch {
		case runes[i] == 'A':
			absent += 1
			continuous_late = 0
			if absent > 1 {
				return false
			}
		case runes[i] == 'L':
			continuous_late += 1
			if continuous_late > 2 {
				return false
			}
		case runes[i] == 'P':
			continuous_late = 0
		}
	}
	return true
}

func main() {
	fmt.Println(checkRecord("PPALLP"))
	fmt.Println(checkRecord("PPALLL"))
}
