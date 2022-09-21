"""LeetCode 79. Word Search"""

from typing import List


# --- Begin submission ---
def search(a, amap, k, board, word, done, out):
    if k == len(word) - 1:
        done[0] = True
        out[0] = True
    else:
        q, r = a[k]
        k += 1
        cands = []
        if q != 0:
            cands.append((q - 1, r))
        if q != len(board) - 1:
            cands.append((q + 1, r))
        if r != 0:
            cands.append((q, r - 1))
        if r != len(board[0]) - 1:
            cands.append((q, r + 1))
        for x, y in cands:
            if word[k] == board[x][y] and not amap[x][y]:
                a[k] = (x, y)
                amap[x][y] = True
                search(a, amap, k, board, word, done, out)
                amap[x][y] = False
            if done[0]:
                return


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        done = [False]
        out = [False]
        starts = []
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c == word[0]:
                    starts.append((i, j))
        for start in starts:
            a = [(0, 0)] * len(word)
            a[0] = start
            amap = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
            amap[start[0]][start[1]] = True
            search(a, amap, 0, board, word, done, out)
            if out[0]:
                return True
        return False


# --- End submission ---
