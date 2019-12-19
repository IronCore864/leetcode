from heapq import heapify, nlargest, heapreplace, heappush
    

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = nums
        heapify(self.h)
        while len(self.h) > k:
            heapq.heappop(self.h)


    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heappush(self.h, val)
        elif val > self.h[0]:
            heapreplace(self.h, val)
        return self.h[0]
