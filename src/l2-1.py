"""LeetCode 402. Remove K Digits"""

# Ex.
# Input: num = "1432219", k = 3
# Output: "1219"
# 1432219
#  012

# Comments:
# My solution is annoyingly slow because list.pop(i) is O(n) in the worst case.
# Having looked at faster solutions, the best approaches build up their output
# in a stack, popping the top element when it's larger than the element under
# consideration. This is similar to my approach, except that they manage to
# always get O(1) list.pop because of the stack.


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numl = list(num)
        i = 0
        while k > 0:
            if i == len(numl) - 1 or numl[i] > numl[i + 1]:
                numl.pop(i)
                i = max(0, i - 1)
                k -= 1
            else:
                i += 1

        if len(numl) == 0:
            numl = ["0"]
        else:
            i = 0
            while numl[i] == "0" and i < len(numl) - 1:
                i += 1
            numl = numl[i:]

        return "".join(numl)
