import copy
import random

from collections import deque
from math import inf
from typing import Tuple


# TODO: unit test
def unweighted_adj_list_to_matrix(g):
    gm = [[0] * len(g) for _ in range(len(g))]
    for i in range(len(g)):
        for v in g[i]:
            gm[i][v] = 1
    return gm


def unweighted_adj_matrix_to_list(g):
    gl = [[] for _ in range(len(g))]
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j]:
                gl[i].append(j)
    return gl


def random_adj_matrix(n):
    adj_mat = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            adj_mat[i][j] = random.randint(0, 1)
    for i in range(n):
        for j in range(0, i):
            adj_mat[i][j] = adj_mat[j][i]
    return adj_mat


def random_adj_list(n):
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (
                i != j
                and j not in adj_list[i]
                and i not in adj_list[j]
                and random.randint(0, 1)
            ):
                adj_list[i].append(j)
                adj_list[j].append(i)
    for i in range(n):
        adj_list[i].sort()
    return adj_list


def k_n(n):
    return [[1 if i != j else 0 for j in range(n)] for i in range(n)]


def random_permutation_matrix(n):
    p = list(range(n))
    random.shuffle(p)
    return [[1 if i == p[j] else 0 for i in range(n)] for j in range(n)]


def randomly_permute_vertices(g):
    n = len(g)
    p = list(range(n))
    random.shuffle(p)
    h = copy.deepcopy(g)
    for i in range(n):
        for j in range(n):
            g[i][j] = h[p[i]][p[j]]
    return g


def mul_adj(g, h):
    n = len(g)
    if n != len(h):
        raise ValueError("Matrix dimensions must agree")
    out = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                out[i][j] += g[i][k] * h[k][j]
    return out


def floyd_warshall(adj_mat, zeros_are_edges=True):
    n = len(adj_mat)
    spm = copy.deepcopy(adj_mat)
    if not zeros_are_edges:
        for i in range(n):
            for j in range(n):
                if spm[i][j] == 0:
                    spm[i][j] = inf

    for k in range(n):
        for i in range(n):
            for j in range(n):
                through_k = spm[i][k] + spm[k][j]
                if through_k < spm[i][j]:
                    spm[i][j] = through_k
    return spm


# TODO: unit test
def bfs_adj_list(g, s) -> Tuple[list[int], list[int]]:
    discovered = [False] * len(g)
    dist = [0] * len(g)
    parent = [None] * len(g)

    q = deque([s])
    discovered[s] = True
    while len(q) > 0:
        u = q.popleft()
        for v in g[u]:
            if not discovered[v]:
                q.append(v)
                discovered[v] = True
                dist[v] = dist[u] + 1
                parent[v] = u

    return dist, parent


def filtered_adj_list(g, keep) -> list[list[int]]:
    """
    g: a graph in adjacency list form.
    keep: a list of vertex indices to keep.
    """
    keep_long = [False] * len(g)
    for _, v in enumerate(keep):
        keep_long[v] = True

    gprime = [
        list(filter(lambda x: keep_long[x], g[i]))
        for i, kp in enumerate(keep_long)
        if kp
    ]

    inv = [None] * len(g)
    for i, v in enumerate(keep):
        inv[v] = i

    for es in gprime:
        for v in range(len(es)):
            es[v] = inv[es[v]]
    return gprime
