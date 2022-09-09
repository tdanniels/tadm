import copy
import random

from math import inf


def random_adj_matrix(n):
    adj_mat = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            adj_mat[i][j] = random.randint(0, 1)
    for i in range(n):
        for j in range(0, i):
            adj_mat[i][j] = adj_mat[j][i]
    return adj_mat


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


def adj_matrix_multiply(g, h):
    n = len(g)
    if n != len(h):
        raise ValueError("Matrix dimensions must agree")
    out = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                out[i][j] += g[i][k] * h[k][j]
    return out
