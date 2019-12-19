package main

import (
	"container/heap"
	"fmt"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type KthLargest struct {
	h *IntHeap
	k int
}

func Constructor(k int, nums []int) KthLargest {
	h := IntHeap(nums)
	heap.Init(&h)
	for len(h) > k {
		heap.Pop(&h)
	}
	return KthLargest{&h, k}
}

func (this *KthLargest) Add(val int) int {
	if len(*this.h) < this.k {
		heap.Push(this.h, val)
	} else if val > (*this.h)[0] {
		heap.Push(this.h, val)
		heap.Pop(this.h)
	}
	return (*this.h)[0]
}

func main() {
	obj := Constructor(3, []int{4, 5, 8, 2})
	fmt.Println(obj.Add(3))
	fmt.Println(obj.Add(5))
	fmt.Println(obj.Add(10))
	fmt.Println(obj.Add(9))
	fmt.Println(obj.Add(4))
}
