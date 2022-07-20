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
        numsd = [[v] * d[v] for v in d]
        numsd = [v for vs in numsd for v in vs]

        pair_table = dict()
        for i in range(len(numsd)):
            for j in range(i + 1, len(numsd)):
                try:
                    pair_table[numsd[i] + numsd[j]].append((i, j))
                except KeyError:
                    pair_table[numsd[i] + numsd[j]] = [(i, j)]

        out = set()
        for k in range(len(numsd)):
            nk = numsd[k]
            for l in range(k + 1, len(numsd)):
                try:
                    x = pair_table[target - (numsd[k] + numsd[l])]
                except KeyError:
                    continue
                nl = numsd[l]
                for i, j in x:
                    if i != k and i != l and j != k and j != l:
                        ns = [numsd[i], numsd[j], nk, nl]
                        ns.sort()
                        out.add(tuple(ns))

        return [list(t) for t in out]
