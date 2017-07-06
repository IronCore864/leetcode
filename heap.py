class heap(object):
    @staticmethod
    def insert(h, n):
        h.append(n)
        current_idx = len(h) - 1
        parent_idx = (current_idx - 1) // 2
        while h[current_idx] < h[parent_idx] and parent_idx >= 0:
            h[current_idx], h[parent_idx] = h[parent_idx], h[current_idx]
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    @staticmethod
    def pop(h):
        h[0] = h[-1]
        h.pop()
        current_idx = 0
        left_child_idx = (current_idx + 1) * 2 - 1
        right_child_idx = (current_idx + 1) * 2
        while left_child_idx < len(h) and right_child_idx < len(h) and h[current_idx] > max(h[left_child_idx],
                                                                                            h[right_child_idx]):
            next_idx = left_child_idx if h[left_child_idx] < h[right_child_idx] else right_child_idx
            h[current_idx], h[next_idx] = h[next_idx], h[current_idx]
            current_idx = next_idx
            left_child_idx = (current_idx + 1) * 2 - 1
            right_child_idx = (current_idx + 1) * 2
        if left_child_idx < len(h) and h[left_child_idx] < h[current_idx]:
            h[current_idx], h[left_child_idx] = h[left_child_idx], h[current_idx]


class Solution():
    def top_k(self, nums, k):
        h = []
        for n in nums:
            if len(h) < k:
                heap.insert(h, n)
            else:
                if n > h[0]:
                    heap.pop(h)
                    heap.insert(h, n)
        return h


s = Solution()
print(s.top_k([1, 2, 5, 10, 3, 7, 11, 15, 17, 20, 9, 15, 8, 16], 3))
