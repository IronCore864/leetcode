package main

import "fmt"

type Node struct {
	val         bool
	isLeaf      bool
	topLeft     *Node
	topRight    *Node
	bottomLeft  *Node
	bottomRight *Node
}

func intersect(t1, t2 *Node) *Node {
	var res *Node
	if t1.isLeaf || t2.isLeaf {
		if t1.isLeaf && t2.isLeaf {
			res = &Node{t1.val || t2.val, true, nil, nil, nil, nil}
		} else if t1.val == true || t2.val == true {
			res = &Node{true, true, nil, nil, nil, nil}
		} else if t1.isLeaf {
			res = t2
		} else if t2.isLeaf {
			res = t1
		}
	} else {
		tl := intersect(t1.topLeft, t2.topLeft)
		tr := intersect(t1.topRight, t2.topRight)
		bl := intersect(t1.bottomLeft, t2.bottomLeft)
		br := intersect(t1.bottomRight, t2.bottomRight)
		if tl.val == tr.val == bl.val == br.val && (tl.isLeaf && tr.isLeaf && bl.isLeaf && br.isLeaf) {
			res = &Node{tl.val, true, nil, nil, nil, nil}
		} else {
			res = &Node{false, false, tl, tr, bl, br}
		}
	}
	return res
}

func main() {
	t1 := Node{false, false, &Node{false, true, nil, nil, nil, nil}, &Node{false, true, nil, nil, nil, nil}, &Node{true, true, nil, nil, nil, nil}, &Node{true, true, nil, nil, nil, nil}}
	t2 := Node{false, false, &Node{true, true, nil, nil, nil, nil}, &Node{true, true, nil, nil, nil, nil}, &Node{false, true, nil, nil, nil, nil}, &Node{false, true, nil, nil, nil, nil}}
	res := intersect(&t1, &t2)
	fmt.Println(res)
}
