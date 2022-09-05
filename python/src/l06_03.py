"""
LeetCode 1334. Find the City With the Smallest Number of Neighbors at a
Threshold Distance
"""

from typing import List

# --- Begin submission ---
from math import inf


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        adj = [[inf for _ in range(n)] for _ in range(n)]
        for i, j, w in edges:
            adj[i][j] = w
            adj[j][i] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    through_k = adj[i][k] + adj[k][j]
                    if through_k < adj[i][j]:
                        adj[i][j] = through_k
        min_count = inf
        min_city = None
        for i in range(n):
            under_threshold = 0
            for j in range(n):
                if i == j:
                    continue
                if adj[i][j] <= distanceThreshold:
                    under_threshold += 1
            if under_threshold <= min_count:
                min_count = under_threshold
                min_city = i
        return min_city


# --- End submission ---
