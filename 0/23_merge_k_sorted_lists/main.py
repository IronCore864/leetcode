from typing import List, Optional
from heapq import heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        cur = head
        h = []

        for i in range(len(lists)):
            if lists[i]:
                heappush(h, (lists[i].val, i))

        while h:
            v, i = heappop(h)
            cur.next = ListNode(v)
            cur = cur.next
            if lists[i].next:
                lists[i] = lists[i].next
                heappush(h, (lists[i].val, i))

        return head.next
