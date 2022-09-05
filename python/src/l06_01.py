"""LeetCode 787. Cheapest Flights Within K Stops"""

from typing import List

# --- Begin submission ---
import math
from math import inf


def to_adj_lst(n, flights):
    adj = [[] for _ in range(n)]
    for fr, to, price in flights:
        adj[fr].append((to, price))
    return adj


def cheapest(adj_lst, src, dst, kmax):
    dist = [[inf for _ in range(kmax + 2)] for _ in range(len(adj_lst))]
    dist[src][0] = 0
    for k in range(kmax + 1):
        for u in range(len(adj_lst)):
            for v, w in adj_lst[u]:
                if dist[u][k] + w < dist[v][k + 1]:
                    dist[v][k + 1] = dist[u][k] + w
    mincost = inf
    for k in range(kmax + 2):
        if dist[dst][k] < mincost:
            mincost = dist[dst][k]
    return mincost


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj_lst = to_adj_lst(n, flights)
        price = cheapest(adj_lst, src, dst, k)
        if math.isinf(price):
            return -1
        return price


# --- End submission ---
