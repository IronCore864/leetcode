package main

import "fmt"

// MyHashSet is
type MyHashSet struct {
	buckets   [][]int
	size      int
	used      int
	threshold float32
}

// Constructor is
func Constructor() MyHashSet {
	return MyHashSet{make([][]int, 8), 8, 0, 0.618}
}

func (hs *MyHashSet) checkCapacityAndResize() {
	if float32(hs.used)/float32(hs.size) > hs.threshold {
		hs.resize()
	}
}

func (hs *MyHashSet) resize() {
	hs.size *= 2
	hs.used = 0
	newBuckets := make([][]int, hs.size)
	for i := 0; i < len(hs.buckets); i++ {
		for j := 0; j < len(hs.buckets[i]); j++ {
			h := hs.hash(hs.buckets[i][j])
			newBuckets[h] = append(newBuckets[h], hs.buckets[i][j])
			hs.used++
		}
	}
	hs.buckets = newBuckets
}

func (hs *MyHashSet) hash(key int) int {
	return key % hs.size
}

func (hs *MyHashSet) index(key int) (int, int) {
	h := hs.hash(key)
	idx := -1
	for i := 0; i < len(hs.buckets[h]); i++ {
		if hs.buckets[h][i] == key {
			idx = i
			break
		}
	}
	return h, idx
}

// Add is
func (hs *MyHashSet) Add(key int) {
	hs.checkCapacityAndResize()
	b, idx := hs.index(key)
	if idx > -1 {
		return
	}
	hs.buckets[b] = append(hs.buckets[b], key)
	hs.used++
}

// Remove is
func (hs *MyHashSet) Remove(key int) {
	b, idx := hs.index(key)
	if idx == -1 {
		return
	}
	hs.buckets[b][idx] = hs.buckets[b][len(hs.buckets[b])-1]
	hs.buckets[b][len(hs.buckets[b])-1] = 0
	hs.buckets[b] = hs.buckets[b][:len(hs.buckets[b])-1]
}

// Contains is
func (hs *MyHashSet) Contains(key int) bool {
	_, idx := hs.index(key)
	return idx > -1
}

func main() {
	hs := Constructor()
	for i := 0; i < 10; i++ {
		hs.Add(i)
	}
	hs.Remove(2)
	fmt.Println(hs.Contains(1))
	fmt.Println(hs.Contains(2))
	hs.Add(9)
	hs.Remove(19)
	hs.Add(14)
	hs.Remove(19)
	hs.Remove(9)
	hs.Add(0)
	hs.Add(3)
	hs.Add(4)
	hs.Add(0)
	hs.Remove(9)
}
