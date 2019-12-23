class MyHashSet:
    def __init__(self):
        self.size = 8
        self.used = 0
        self.threshold = 0.618
        self.buckets = [[] for _ in range(self.size)]

    def _resize(self):
        self.size *= 2
        self.used = 0
        new_buckets = [[] for _ in range(self.size)]
        for b in self.buckets:
            for k in b:
                h = self._hash(k)
                new_buckets[h].append(k)
                self.used += 1
        self.buckets = new_buckets
        print("Resizing: current size: {} current used: {} new size {}".format(self.size // 2, self.used, self.size))

    def _check_capacity_and_resize(self):
        capacity = self.used / self.size
        if capacity > self.threshold:
            self._resize()

    def add(self, key):
        self._check_capacity_and_resize()
        bucket, idx = self._index(key)
        if idx >= 0:
            return
        bucket.append(key)
        self.used += 1

    def remove(self, key):
        bucket, idx = self._index(key)
        if idx < 0:
            return
        bucket.remove(key)

    def contains(self, key):
        _, idx = self._index(key)
        return idx >= 0

    def _hash(self, key):
        return key % self.size

    def _index(self, key):
        h = self._hash(key)
        bucket = self.buckets[h]
        for i, k in enumerate(bucket):
            if k == key:
                return bucket, i
        return bucket, -1


hs = MyHashSet()
for i in range(10):
    hs.add(i)
hs.remove(2)
print(hs.contains(1))
print(hs.contains(2))
