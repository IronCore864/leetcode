package main

import "fmt"

func nextGreatestLetter(letters []byte, target byte) byte {
	l := len(letters)
	if letters[l-1] <= target {
		return letters[0]
	}
	start, end := 0, l-1
	for start <= end {
		mid := (end-start)/2 + start
		if letters[mid] > target {
			if mid == 0 || letters[mid-1] <= target {
				return letters[mid]
			}
			end = mid - 1
		} else {
			if mid+1 < l && letters[mid+1] > target {
				return letters[mid+1]
			}
			start = mid + 1
		}
	}
	return 0
}

func main() {
	fmt.Println(nextGreatestLetter([]byte{'c', 'f', 'j'}, 'f'))
}
