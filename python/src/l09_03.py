"""996. Number of Squareful Arrays"""

from collections import defaultdict
from typing import List


# --- Begin submission ---
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        valid_neighbours = {
            l: [
                r
                for j, r in enumerate(nums)
                if i != j and ((l + r) ** 0.5).is_integer()
            ]
            for i, l in enumerate(nums)
        }
        a = [0] * (len(nums) + 1)
        k = 0
        out = [0]
        numcount = defaultdict(int)
        for num in nums:
            numcount[num] += 1

        def backtrack(a, k, out):
            if k == len(nums):
                out[0] += 1
            else:
                k += 1
                if k == 1:
                    cands = set(nums)
                else:
                    cands = set(
                        neighb
                        for neighb in valid_neighbours[a[k - 1]]
                        if numcount[neighb]
                    )
                for cand in cands:
                    a[k] = cand
                    numcount[cand] -= 1
                    backtrack(a, k, out)
                    numcount[cand] += 1

        backtrack(a, k, out)
        return out[0]


# --- End submission ---
