"""LeetCode 968. Binary Tree Cameras"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --- Begin submission ---
from math import inf


def dfs(root):
    if not root.left and not root.right:
        # minimum costs of (not covered, covered from below, in covering set)
        return (0, inf, 1)

    l = dfs(root.left) if root.left else (0, 0, inf)
    r = dfs(root.right) if root.right else (0, 0, inf)

    nc = l[1] + r[1]
    cfb = min(l[2] + r[2], l[1] + r[2], l[2] + r[1])
    cs = 1 + min(l) + min(r)

    return (nc, cfb, cs)


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        s = dfs(root)
        return min(s[1], s[2])


# --- End submission ---
