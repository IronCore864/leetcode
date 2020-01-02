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
        # print("Resizing: current size: {} current used: {} new size {}".format(self.size // 2, self.used, self.size))

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
        if current is None and previous is None:
            self.buckets[self._hash(key)] = ListNode(key, value)
            self.used += 1
        elif previous is not None and current is not None:
            current.val = value
        elif previous is not None and current is None:
            previous.next = ListNode(key, value)
            self.used += 1

    def get(self, key: int) -> int:
        previous, current = self._find_node_return_previous_and_current(key)
        return -1 if not previous or not current else current.val

    def remove(self, key: int) -> None:
        previous, current = self._find_node_return_previous_and_current(key)
        if current is None:
            return
        elif previous == current:
            self.buckets[self._hash(key)] = current.next
        else:
            previous.next = current.next
            self.used -= 1


op = ["MyHashMap", "put", "put", "put", "remove", "get", "put", "put", "get", "put", "put", "put", "put", "put", "put",
      "put", "put", "put", "put", "put", "put", "remove", "put", "remove", "put", "put", "remove", "put", "get", "put",
      "get", "put", "put", "put", "put", "put", "get", "put", "remove", "put", "remove", "put", "put", "put", "put",
      "put", "remove", "put", "put", "remove", "put", "put", "put", "get", "get", "put", "remove", "put", "put", "put",
      "get", "put", "put", "put", "remove", "put", "put", "put", "put", "put", "get", "put", "put", "get", "get", "put",
      "remove", "remove", "get", "put", "remove", "put", "remove", "put", "put", "put", "get", "put", "put", "put",
      "remove", "put", "put", "get", "put", "put", "get", "remove", "get", "get", "put"]
param = [[], [24, 31], [58, 35], [59, 88], [84], [62], [2, 22], [44, 70], [24], [24, 42], [58, 99], [74, 29], [40, 66],
         [55, 83], [21, 27], [31, 25], [78, 19], [86, 70], [71, 73], [39, 95], [6, 96], [76], [62, 22], [78], [53, 51],
         [66, 53], [44], [14, 46], [77], [15, 32], [22], [53, 79], [35, 21], [73, 57], [18, 67], [96, 61], [73],
         [58, 77], [6], [5, 58], [17], [25, 14], [16, 13], [4, 37], [47, 43], [14, 79], [35], [7, 13], [78, 85], [27],
         [73, 33], [95, 87], [31, 21], [20], [64], [90, 22], [16], [77, 50], [55, 41], [33, 62], [44], [73, 16],
         [13, 54], [41, 5], [71], [81, 6], [20, 98], [35, 64], [15, 35], [74, 31], [90], [32, 15], [44, 79], [37], [53],
         [22, 80], [24], [10], [7], [53, 61], [65], [63, 99], [47], [97, 68], [7, 0], [9, 25], [97], [93, 13], [92, 43],
         [83, 73], [74], [41, 78], [39, 28], [52], [34, 16], [93, 63], [82], [77], [16], [50], [68, 47]]

hm = MyHashMap()
for i in range(len(op)):
    if op[i] == "MyHashMap":
        hm = MyHashMap()
        continue
    if op[i] == "put":
        print(hm.put(param[i][0], param[i][1]))
    if op[i] == "get":
        print(hm.get(param[i][0]))
    if op[i] == "remove":
        print(hm.remove(param[i][0]))

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
