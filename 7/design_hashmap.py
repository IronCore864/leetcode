package main

import "fmt"

type ListNode struct {
	key  int
	val  int
	next *ListNode
}

type MyHashMap struct {
	buckets            []*ListNode
	size               int
	used               int
	scaleUpThreshold   float32
	scaleDownThreshold float32
}

func Constructor() MyHashMap {
	return MyHashMap{make([]*ListNode, 8), 8, 0, 0.618, 0.1}
}

func (hm *MyHashMap) checkCapacityAndResize() {
	if float32(hm.used)/float32(hm.size) > hm.scaleUpThreshold {
		hm.scaleUp()
	}
	if float32(hm.used)/float32(hm.size) < hm.scaleDownThreshold {
		hm.scaleDown()
	}
}

func (hm *MyHashMap) fillNewBuckets(buckets []*ListNode, size int) []*ListNode {
	newBuckets := make([]*ListNode, size)
	for i := 0; i < len(buckets); i++ {
		current := buckets[i]
		for current != nil {
			h := hm.hash(current.key)
			newBuckets[h] = &ListNode{current.key, current.val, newBuckets[h]}
			hm.used++
			current = current.next
		}
	}
	return newBuckets
}

func (hm *MyHashMap) scaleUp() {
	hm.size *= 2
	hm.used = 0
	hm.buckets = hm.fillNewBuckets(hm.buckets, hm.size)
	fmt.Println("Scaling up", hm.size)
}

func (hm *MyHashMap) scaleDown() {
	hm.size /= 2
	hm.used = 0
	hm.buckets = hm.fillNewBuckets(hm.buckets, hm.size)
	fmt.Println("Scaling down", hm.size)
}

func (hm *MyHashMap) hash(key int) int {
	return key % hm.size
}

func (hm *MyHashMap) searchNodeReturnPreviousCurrent(key int) (*ListNode, *ListNode) {
	h := hm.hash(key)
	current := hm.buckets[h]
	previous := current
	for current != nil && current.key != key {
		previous = current
		current = current.next
	}
	return previous, current
}

func (hm *MyHashMap) Put(key int, value int) {
	hm.checkCapacityAndResize()
	previous, current := hm.searchNodeReturnPreviousCurrent(key)
	if previous == nil {
		hm.buckets[hm.hash(key)] = &ListNode{key, value, nil}
		hm.used++
	} else if current == nil {
		previous.next = &ListNode{key, value, nil}
		hm.used++
	} else if current.val != value {
		current.val = value
	}
}

func (hm *MyHashMap) Get(key int) int {
	previous, current := hm.searchNodeReturnPreviousCurrent(key)
	if previous == nil || current == nil {
		return -1
	}
	return current.val
}

func (hm *MyHashMap) Remove(key int) {
	hm.checkCapacityAndResize()
	previous, current := hm.searchNodeReturnPreviousCurrent(key)
	if current == nil {
		return
	} else if previous == current {
		hm.buckets[hm.hash(key)] = current.next
		hm.used--
	} else {
		previous.next = current.next
		hm.used--
	}
}

func main() {
	hm := Constructor()
	for i := 0; i < 100; i++ {
		hm.Put(i, i)
	}
	for i := 0; i < 100; i++ {
		hm.Remove(i)
	}
}
