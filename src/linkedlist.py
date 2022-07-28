from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class LinkedList:
    value: int
    next: Optional[LinkedList]

    @staticmethod
    def from_list(l: list[int]) -> Optional[LinkedList]:
        if l:
            ll = LinkedList(l[0], LinkedList.from_list(l[1:]))
        else:
            ll = None
        return ll

    def to_list(self) -> list[int]:
        l = []
        cur = self
        while cur is not None:
            l.append(cur.value)
            cur = cur.next
        return l

    def append(self, ll: LinkedList):
        cur = self
        while cur.next is not None:
            cur = cur.next
        cur.next = ll

    # start snippet reverse-ll
    def reverse(self) -> LinkedList:
        """Reverses in-place recursively and returns a reference to the new head."""
        if self.next is None:
            return self
        else:
            new_head = self.next.reverse()
            self.next.next = self
            self.next = None
            return new_head

    def reverse_nr(self) -> LinkedList:
        """Reverses in-place non-recursively and returns a reference to the new head."""
        stack = []
        cur = self
        while cur is not None:
            stack.append(cur)
            cur = cur.next
        new_head = stack[-1]
        while stack:
            node = stack.pop()
            if stack:
                node.next = stack[-1]
            else:
                node.next = None
        return new_head
        # end snippet reverse-ll

    # start snippet tortoise-hare-ll
    def has_loop(self) -> bool:
        tortoise = self
        hare = self
        while True:
            tortoise = tortoise.next
            hare = hare.next
            if tortoise is None or hare is None:
                return False
            maybe_loop = hare
            hare = hare.next
            if hare is None:
                return False
            if tortoise == hare:
                print(f"loop detected: {maybe_loop} -> {tortoise}")
                return True
        # end snippet tortoise-hare-ll


