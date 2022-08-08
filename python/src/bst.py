from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from weakref import proxy


# start snippet bst-def
@dataclass
class BST:
    left: Optional[BST]
    right: Optional[BST]
    parent: Optional[BST]
    value: int
    # end snippet bst-def

    # start snippet bst-eq
    def __eq__(self, o):
        return self.value == o.value and self.left == o.left and self.right == o.right
        # end snippet bst-eq

    def to_list(self) -> list:
        l = []
        if self.left is not None:
            l.append(self.left.to_list())
        l.append(self.value)
        if self.right is not None:
            l.append(self.right.to_list())
        return l

    def find_max(self) -> BST:
        if self.right is None:
            return self
        return self.right.find_max()


def from_list(l: list) -> BST:
    r"""
    Transforms a list of the form [[[0], 1, [2]], 3, [4, [5]]] into
    a BST of the form

                 3
                / \
               1   4
              / \   \
             0   2   5
    """
    return __from_list(l, None)


def __from_list(l: list, parent: Optional[BST]) -> BST:
    children = []
    count = 0
    p = None if parent is None else proxy(parent)
    tree = BST(None, None, p, 0)

    for v in l:
        if type(v) == list:
            if count > 3:
                raise ValueError("Too many items in node")
            children.append(__from_list(v, tree))
            count += 1
        elif type(v) == int:
            if count > 2:
                raise ValueError("Node value in right child position")
            tree.value = v
            count += 1
        else:
            raise ValueError("Invalid item type")

    for c, lr in zip(children, ("left", "right")):
        setattr(tree, lr, c)

    return tree
