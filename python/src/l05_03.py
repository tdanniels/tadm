""" LeetCode 207. Course Schedule"""

from typing import List


# --- Begin submission ---
def to_adj_list(n, edges) -> List[List[int]]:
    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[v].append(u)
    return adj_list


def is_dag(adj_list, u, discovered, processed) -> bool:
    discovered[u] = True
    for v in adj_list[u]:
        if discovered[v] and not processed[v]:
            return False
        if not discovered[v]:
            if not is_dag(adj_list, v, discovered, processed):
                return False
    processed[u] = True
    return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = to_adj_list(numCourses, prerequisites)
        discovered = [False] * len(adj_list)
        processed = [False] * len(adj_list)
        for u in range(len(adj_list)):
            if not discovered[u]:
                if not is_dag(adj_list, u, discovered, processed):
                    return False
        return True


# --- End submission ---
