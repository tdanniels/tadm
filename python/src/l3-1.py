"""LeetCode 98. Validate Binary Search Tree"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --- Begin submission ---
from math import inf


class Solution:
    def __init__(self):
        self.rightmax = [inf]
        self.leftmin = [-inf]

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if root.left:
            self.rightmax.append(root.val)
            if not (
                root.left.val < root.val
                and root.left.val > self.leftmin[-1]
                and self.isValidBST(root.left)
            ):
                return False
            self.rightmax.pop()

        if root.right:
            self.leftmin.append(root.val)
            if not (
                root.right.val > root.val
                and root.right.val < self.rightmax[-1]
                and self.isValidBST(root.right)
            ):
                return False
            self.leftmin.pop()

        return True


# --- End submission ---
