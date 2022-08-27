""" LeetCode 310. Minimum Height Trees"""

from typing import List


# --- Begin submission ---
from collections import deque


def to_adj_list(n, edges) -> List[List[int]]:
    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list


def bfs_max_dist(adj_list, s):
    discovered = [False] * len(adj_list)
    dist = [0] * len(adj_list)
    parent = [None] * len(adj_list)

    q = deque([s])
    discovered[s] = True
    while len(q) > 0:
        u = q.popleft()
        for v in adj_list[u]:
            if not discovered[v]:
                q.append(v)
                discovered[v] = True
                dist[v] = dist[u] + 1
                parent[v] = u

    return max(enumerate(dist), key=lambda x: x[1])[0], parent


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = to_adj_list(n, edges)
        max_node_1 = bfs_max_dist(adj_list, 0)[0]
        max_node_2, parent = bfs_max_dist(adj_list, max_node_1)

        child = max_node_2
        longest_path = [child]
        while parent[child] is not None:
            longest_path.append(parent[child])
            child = parent[child]

        out = [longest_path[len(longest_path) // 2]]
        if len(longest_path) % 2 == 0:
            out.append(longest_path[len(longest_path) // 2 - 1])
        return out


# --- End submission ---


if __name__ == "__main__":
    s = Solution()
    ans = s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
    print(ans)
    assert ans == [1]
