class ListNode:
    def __init__(self, key=None, value=None, next_node=None):
        self.key = key
        self.val = value
        self.next = next_node


class MyHashMap:
    def __init__(self):
        self.size = 8
        self.used = 0
        self.threshold = 0.618
        self.buckets = [None] * self.size

    def _resize(self):
        self.size *= 2
        self.used = 0
        new_buckets = [None] * self.size
        for b in self.buckets:
            current = b
            while current:
                h = self._hash(current.key)
                new_buckets[h] = ListNode(current.key, current.val, new_buckets[h])
                self.used += 1
                current = current.next
        self.buckets = new_buckets
        print("Resizing: current size: {} current used: {} new size {}".format(self.size // 2, self.used, self.size))

    def _check_capacity_and_resize(self):
        capacity = self.used / self.size
        if capacity > self.threshold:
            self._resize()

    def _hash(self, key):
        return key % self.size

    def _find_node_return_previous_and_current(self, key):
        h = self._hash(key)
        current = previous = self.buckets[h]
        while current and current.key != key:
            previous = current
            current = current.next
        return previous, current

    def put(self, key: int, value: int) -> None:
        self._check_capacity_and_resize()
        previous, current = self._find_node_return_previous_and_current(key)
        if not previous:
            self.buckets[self._hash(key)] = ListNode(key, value)
            self.used += 1
        elif not current:
            previous.next = ListNode(key, value)
            self.used += 1
        elif current.key == key:
            current.val = value

    def get(self, key: int) -> int:
        previous, current = self._find_node_return_previous_and_current(key)
        return -1 if not previous or not current else current.val

    def remove(self, key: int) -> None:
        previous, current = self._find_node_return_previous_and_current(key)
        if not previous:
            return
        elif previous == current:
            self.buckets[self._hash(key)] = None
            self.used -= 1
        elif current is not None:
            previous.next = None
            self.used -= 1


print("simple test")
hm = MyHashMap()
for i in range(0, 10):
    hm.put(i, i)
hm.remove(2)
hm.remove(11)
print(hm.get(1))
print(hm.get(2))

print("test resizing")
hm = MyHashMap()
for i in range(0, 10):
    hm.put(i * 8, i * 8)
print(hm.buckets)
c = hm.buckets[0]
while c:
    print(c.val)
    c = c.next
c = hm.buckets[8]
while c:
    print(c.val)
    c = c.next
