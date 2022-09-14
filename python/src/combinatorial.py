import copy
import itertools
from typing import List, Tuple

import graph


# start snippet backtrack
def backtrack(a, k, finished, solver):
    if solver.is_soln(a, k, finished):
        solver.process_soln(a, k, finished)
    else:
        k += 1
        cands = solver.construct_cands(a, k, finished)
        for cand in cands:
            a[k] = cand
            solver.make_move(a, k, finished)
            backtrack(a, k, finished, solver)
            solver.unmake_move(a, k, finished)
            if finished[0]:
                return


class Solver:
    def is_soln(self, a, k, finished):
        pass

    def process_soln(self, a, k, finished):
        pass

    def construct_cands(self, a, k, finished):
        pass

    def make_move(self, a, k, finished):
        pass

    def unmake_move(self, a, k, finished):
        pass


# end snippet backtrack


# start snippet derangements
class DerangementsSolver(Solver):
    def __init__(self, n):
        self.n = n
        self.out = []

    def is_soln(self, a, k, finished):
        return k == self.n

    def process_soln(self, a, k, finished):
        self.out.append(a[1:])

    def construct_cands(self, a, k, finished):
        cands = []
        in_derangement = [False for _ in range(self.n + 1)]
        for i in range(1, k):
            in_derangement[a[i]] = True

        for i in range(1, self.n + 1):
            if i != k and not in_derangement[i]:
                cands.append(i)
        return cands


def derangements(n) -> List[int]:
    a = [0] * (n + 1)
    finished = [False]
    s = DerangementsSolver(n)
    backtrack(a, 0, finished, s)
    return s.out


# end snippet derangements


class CombinationsSolver(Solver):
    def __init__(self, n, r):
        self.n = n
        self.r = r
        self.out = []

    def is_soln(self, a, k, finished):
        return k == self.r

    def process_soln(self, a, k, finished):
        if self.r == 0:
            self.out.append(tuple())
        else:
            self.out.append(tuple(a[1:]))

    def construct_cands(self, a, k, finished):
        if self.n < self.r or self.r == 0:
            return []
        return [i for i in range(a[k - 1] + 1, self.n - self.r + k)]


def combinations(n, r) -> List[Tuple[int]]:
    a = [-1] * (r + 1)
    finished = [False]
    s = CombinationsSolver(n, r)
    backtrack(a, 0, finished, s)
    return s.out


# start snippet graph-isomorphism
class GraphIsomorphismSolver(Solver):
    def __init__(self, g, h):
        self.gr = [g, h]
        self.n = len(self.gr[0])
        self.d = []
        self.spm = []
        self.lkp = [[], []]
        self.out = False
        for r in (0, 1):
            self.d.append(
                [len(list(filter(None, self.gr[r][i]))) for i in range(self.n)]
            )
            self.spm.append(graph.floyd_warshall(self.gr[r], zeros_are_edges=False))
            for i in range(self.n):
                self.spm[r][i].sort()
                if i == 0:
                    self.lkp[r].append(copy.deepcopy(self.gr[r]))
                else:
                    self.lkp[r].append(graph.mul_adj(self.lkp[r][i - 1], self.gr[r]))
            for i in range(self.n):
                for j in range(self.n):
                    self.lkp[r][i][j].sort()
        self.equiv = [[] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                eq = True
                if self.d[0][i] != self.d[1][j]:
                    continue
                if self.spm[0][i] != self.spm[1][j]:
                    continue
                for k in range(self.n):
                    if self.lkp[0][k][i] != self.lkp[1][k][j]:
                        eq = False
                        break
                if eq:
                    self.equiv[i].append(j)

    def is_soln(self, a, k, finished):
        if k != self.n:
            return False
        for i in range(self.n):
            for j in range(self.n):
                if self.gr[0][i][j] != self.gr[1][a[i + 1]][a[j + 1]]:
                    return False
        return True

    def process_soln(self, a, k, finished):
        self.out = True
        finished[0] = True

    def construct_cands(self, a, k, finished):
        cands = []
        in_iso = [False for _ in range(self.n)]
        for i in range(1, k):
            in_iso[a[i]] = True

        for i in self.equiv[k - 1]:
            if not in_iso[i]:
                cands.append(i)
        return cands


def graph_isomorphism(g, h) -> bool:
    if len(g) != len(h):
        return False

    a = [0] * (len(g) + 1)
    finished = [False]
    s = GraphIsomorphismSolver(g, h)
    backtrack(a, 0, finished, s)
    return s.out


# end snippet graph-isomorphism


# start snippet subgraph-isomorphism
class SubgraphIsomorphismSolver(Solver):
    def __init__(self, g, h):
        self.n = len(g)
        self.g = g
        self.h = h
        self.deg_g = [len(list(filter(None, g[i]))) for i in range(self.n)]
        self.edges_h = [
            [j for j, e in enumerate(h[i]) if e != 0] for i in range(len(h))
        ]
        self.out = False

    def is_soln(self, a, k, finished):
        if k != self.n:
            return False
        subg = self.a_to_subg(a)
        for i in range(self.n):
            for j in range(self.n):
                if self.g[i][j] != subg[i][j]:
                    return False
        return True

    def process_soln(self, a, k, finished):
        self.out = True
        finished[0] = True

    def construct_cands(self, a, k, finished):
        if k > self.n:
            return []
        cands = []
        in_subg = [False for _ in range(len(self.h))]
        for i in range(k - 1):
            in_subg[a[i + 1][0]] = True

        for v in range(len(self.h)):
            if in_subg[v]:
                continue
            for es in itertools.combinations(self.edges_h[v], self.deg_g[k - 1]):
                cands.append((v, es))
        return cands

    def a_to_subg(self, a):
        subg = [[0 for _ in range(self.n)] for _ in range(self.n)]
        vh_to_vg = [0] * len(self.h)
        for vg, vh in enumerate(a[1:]):
            vh_to_vg[vh[0]] = vg
        for i, (v, es) in enumerate(a[1:]):
            for e in es:
                subg[i][vh_to_vg[e]] = self.h[v][e]
        return subg


def subgraph_isomorphism(g, h) -> bool:
    a = [(-1, 0)] * (len(g) + 1)
    finished = [False]
    s = SubgraphIsomorphismSolver(g, h)
    backtrack(a, 0, finished, s)
    return s.out


# end snippet subgraph-isomorphism


# start snippet subgraph-isomorphism-subproblems
def hamiltonian_cycle_sgi(g) -> bool:
    n = len(g)
    hcg = [[1 if j == (i + 1) % n else 0 for j in range(n)] for i in range(n)]
    return subgraph_isomorphism(hcg, g)


def clique_sgi(g) -> int:
    n = len(g)
    maxclique = 0
    for i in range(1, n + 1):
        if subgraph_isomorphism(graph.k_n(i), g):
            maxclique = i
        else:
            break
    return maxclique


def independent_set_sgi(g) -> int:
    n = len(g)
    gprime = [[0 if g[i][j] != 0 or i == j else 1 for j in range(n)] for i in range(n)]
    return clique_sgi(gprime)


def graph_isomorphism_sgi(g, h) -> bool:
    return subgraph_isomorphism(g, h) and subgraph_isomorphism(h, g)


# end snippet subgraph-isomorphism-subproblems
