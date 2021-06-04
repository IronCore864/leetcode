class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.map = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.len = 0

    def delete_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def add_to_head(self, node):
        node.next = self.head.next
        node.next.pre = node
        node.pre = self.head
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        else:
            node = self.map[key]
            self.delete_node(node)
            self.add_to_head(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.delete_node(node)
            self.add_to_head(node)
        else:
            node = Node(key, value)
            self.map[key] = node
            if self.len < self.capacity:
                self.len += 1
                self.add_to_head(node)
            else:
                del self.map[self.tail.pre.key]
                self.delete_node(self.tail.pre)
                self.add_to_head(node)


if __name__ == '__main__':
    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))
    obj.put(3, 3)
    print(obj.get(2))
    obj.put(4, 4)
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))
