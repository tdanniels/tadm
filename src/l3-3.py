""" LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --- Begin submission ---
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = preorder[0]
        root_ino_idx = inorder.index(root)

        ino_left = inorder[:root_ino_idx]
        pre_left = preorder[1 : 1 + len(ino_left)]
        if ino_left:
            left = self.buildTree(pre_left, ino_left)
        else:
            left = None

        ino_right = inorder[root_ino_idx + 1 :]
        pre_right = preorder[1 + len(ino_left) :]
        if ino_right:
            right = self.buildTree(pre_right, ino_right)
        else:
            right = None

        return TreeNode(root, left, right)


# --- End submission ---

# Comments: the original solution did a lot of unnecessary copying. This version
# passes indices instead of slice copies.

# Note: rename to `Solution` if actually submitting.

# --- Begin submission 2 ---
class Solution2:
    def _buildTree(
        self,
        preorder,
        preorder_begin,
        preorder_end,
        inorder,
        inorder_begin,
        inorder_end,
    ):
        root = preorder[preorder_begin]
        root_ino_idx = inorder.index(root, inorder_begin, inorder_end)

        ino_left_begin = inorder_begin
        ino_left_end = root_ino_idx
        pre_left_begin = preorder_begin + 1
        pre_left_end = 1 + (root_ino_idx - inorder_begin)
        if ino_left_end - ino_left_begin > 0:
            left = self._buildTree(
                preorder,
                pre_left_begin,
                pre_left_end,
                inorder,
                ino_left_begin,
                ino_left_end,
            )
        else:
            left = None

        ino_right_begin = root_ino_idx + 1
        ino_right_end = inorder_end
        pre_right_begin = preorder_begin + 1 + (ino_left_end - ino_left_begin)
        pre_right_end = preorder_end
        if ino_right_end - ino_right_begin > 0:
            right = self._buildTree(
                preorder,
                pre_right_begin,
                pre_right_end,
                inorder,
                ino_right_begin,
                ino_right_end,
            )
        else:
            right = None

        return TreeNode(root, left, right)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self._buildTree(preorder, 0, len(preorder), inorder, 0, len(inorder))


# --- End submission 2 ---
