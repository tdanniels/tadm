from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # De-duplicate `nums`, allowing up to 4 of each value.
        d = dict()
        for v in nums:
            try:
                if d[v] < 4:
                    d[v] += 1
            except KeyError:
                d[v] = 1
        nums = [[v] * d[v] for v in d]
        nums = [v for vs in nums for v in vs]

        pair_table = dict()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                try:
                    pair_table[nums[i] + nums[j]].append((i, j))
                except KeyError:
                    pair_table[nums[i] + nums[j]] = [(i, j)]

        out = set()
        for k in range(len(nums)):
            nk = nums[k]
            for l in range(k + 1, len(nums)):
                try:
                    x = pair_table[target - (nums[k] + nums[l])]
                except KeyError:
                    continue
                nl = nums[l]
                for i, j in x:
                    if i != k and i != l and j != k and j != l:
                        ns = [nums[i], nums[j], nk, nl]
                        ns.sort()
                        out.add(tuple(ns))

        return [list(t) for t in out]


if __name__ == "__main__":
    s = Solution()
    assert sorted([sorted(l) for l in s.fourSum([1, 0, -1, 0, -2, 2], 0)]) == sorted(
        sorted(l) for l in [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    )
    assert s.fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
