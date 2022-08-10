"""LeetCode 23. Merge k Sorted Lists"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# --- Begin submission ---
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        out = None
        current = None

        q = [(l.val, i) for i, l in enumerate(lists) if l]
        heapq.heapify(q)
        for _, i in q:
            lists[i] = lists[i].next

        while q:
            v, i = q[0]
            if lists[i]:
                heapq.heapreplace(q, (lists[i].val, i))
                lists[i] = lists[i].next
            else:
                heapq.heappop(q)

            if out is None:
                out = ListNode(v)
                current = out
            else:
                current.next = ListNode(v)
                current = current.next
        return out


# --- End submission ---
