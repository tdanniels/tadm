"""LeetCode 148. Sort List"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Comments: this certainly isn't the fastest way to sort a linked list,
# but it's $O(n\lg{n})$ time and $O(1)$ space, which the problem asks for.


# --- Begin submission ---
from typing import Optional, Tuple


def find_mid(head: ListNode, tail: ListNode) -> ListNode:
    i = 0
    node = head
    while node is not tail:
        node = node.next
        i += 1

    sought = i // 2
    i = 0
    node = head
    while i < sought:
        node = node.next
        i += 1

    return node


def find_tail(head: ListNode) -> ListNode:
    while head.next:
        head = head.next
    return head


def mergesort(head: ListNode, tail: ListNode) -> Tuple[ListNode, int]:
    if head is tail:
        return head, 1

    mid = find_mid(head, tail)
    midright, len_right = mergesort(mid.next, tail)
    head, len_left = mergesort(head, mid)
    return merge(head, len_left, midright, len_right)


def merge(
    head: ListNode, len_left: int, midright: ListNode, len_right: int
) -> Tuple[ListNode, int]:
    left = head
    right = midright
    i = 0
    j = 0

    if left.val <= right.val:
        newhead = left
        left = left.next
        i += 1
    else:
        newhead = right
        right = right.next
        j += 1
    current = newhead

    while i < len_left and j < len_right:
        if left.val <= right.val:
            current.next = left
            current = current.next
            left = left.next
            i += 1
        else:
            current.next = right
            current = current.next
            right = right.next
            j += 1

    while i < len_left:
        current.next = left
        current = current.next
        left = left.next
        i += 1
    while j < len_right:
        current.next = right
        current = current.next
        right = right.next
        j += 1

    current.next = None
    return newhead, len_left + len_right


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        return mergesort(head, find_tail(head))[0]


# --- End submission ---
