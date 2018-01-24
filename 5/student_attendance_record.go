package main

import "fmt"

func checkRecord(s string) bool {
	absent := 0
	continuousLate := 0

	runes := []rune(s)
	for i := 0; i < len(runes); i++ {
		switch {
		case runes[i] == 'A':
			absent += 1
			continuousLate = 0
			if absent > 1 {
				return false
			}
		case runes[i] == 'L':
			continuousLate += 1
			if continuousLate > 2 {
				return false
			}
		case runes[i] == 'P':
			continuousLate = 0
		}
	}
	return true
}

func main() {
	fmt.Println(checkRecord("PPALLP"))
	fmt.Println(checkRecord("PPALLL"))
}
