"""1339. Maximum Product of Splitted Binary Tree"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --- Begin submission ---
def dfs(root, sums):
    if not root:
        return 0
    s = root.val + dfs(root.left, sums) + dfs(root.right, sums)
    sums.append(s)
    return s


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []
        treesum = dfs(root, sums)
        return max((treesum - s) * s for s in sums) % 1_000_000_007


# --- End submission ---
