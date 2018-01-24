package main

import "fmt"

func checkRecord(s string) bool {
	absent := 0
	continuousLate := 0

	for _, c := range s {
		switch {
		case c == 'A':
			absent += 1
			continuousLate = 0
			if absent > 1 {
				return false
			}
		case c == 'L':
			continuousLate += 1
			if continuousLate > 2 {
				return false
			}
		case c == 'P':
			continuousLate = 0
		}
	}
	return true
}

func main() {
	fmt.Println(checkRecord("PPALLP"))
	fmt.Println(checkRecord("PPALLL"))
}
