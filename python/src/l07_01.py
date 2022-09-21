"""LeetCode 78. Subsets"""

from typing import List


# --- Begin submission ---
def solve(a, k, nums, out):
    if k == len(nums):
        subset = [nums[i] for i in range(k) if a[i]]
        out.append(subset)
    else:
        a[k] = False
        solve(a, k + 1, nums, out)
        a[k] = True
        solve(a, k + 1, nums, out)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        a = [False] * len(nums)
        k = 0
        solve(a, k, nums, out)
        return out


# --- End submission ---
