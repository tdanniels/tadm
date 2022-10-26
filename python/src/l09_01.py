"""494. Target Sum"""

from collections import defaultdict
from typing import List


# --- Begin submission ---
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dpa = [defaultdict(int) for _ in range(len(nums))]
        dpa[0][nums[0]] += 1
        dpa[0][-nums[0]] += 1

        for i in range(1, len(nums)):
            for j, v in dpa[i - 1].items():
                dpa[i][j + nums[i]] += v
                dpa[i][j - nums[i]] += v
        return dpa[len(nums) - 1][target]


# --- End submission ---
