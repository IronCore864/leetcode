"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf or quadTree2.isLeaf:
            if quadTree1.isLeaf and quadTree2.isLeaf:
                node = Node(quadTree1.val|quadTree2.val, True)
                return node
            elif quadTree1.val==True or quadTree2.val==True:
                node = Node(True, True)
                return node
            elif quadTree1.isLeaf:
                return quadTree2
            elif quadTree2.isLeaf:
                return quadTree1
        else:
            tl = self.intersect(quadTree1.topLeft,quadTree2.topLeft)
            tr = self.intersect(quadTree1.topRight,quadTree2.topRight)
            bl = self.intersect(quadTree1.bottomLeft,quadTree2.bottomLeft)
            br = self.intersect(quadTree1.bottomRight,quadTree2.bottomRight) 
            if tl.val==tr.val==bl.val==br.val and (tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf):
                return Node(tl.val,True)
            return Node(None,False,tl,tr,bl,br)
