package main

import (
    "fmt"
    "sort"
)

func arrayPairSum(nums []int) int {
    sort.Ints(nums)
    sum := 0
    for i := 0; i < len(nums); i += 2 {
        sum += nums[i]
    }
    fmt.Println(sum)
    return sum
}

func main() {
    a := []int{1, 3, 2, 4}
    arrayPairSum(a)
}
