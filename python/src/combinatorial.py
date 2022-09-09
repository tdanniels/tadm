import copy
from typing import List

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
def derangements(n) -> List[int]:
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

    a = [0] * (n + 1)
    finished = [False]
    s = DerangementsSolver(n)
    backtrack(a, 0, finished, s)
    return s.out


# end snippet derangements


# start snippet graph-isomorphism
def graph_isomorphism(g, h) -> bool:
    class GraphIsomorphismSolver(Solver):
        def __init__(self, g, h):
            self.g = g
            self.h = h
            self.n = len(g)
            self.deg_g = [len(list(filter(None, self.g[i]))) for i in range(self.n)]
            self.deg_h = [len(list(filter(None, self.h[i]))) for i in range(self.n)]
            self.spm_g = graph.floyd_warshall(g, zeros_are_edges=False)
            self.spm_h = graph.floyd_warshall(h, zeros_are_edges=False)
            self.lkp_g = []
            self.lkp_h = []
            for i in range(self.n):
                self.spm_g[i].sort()
                self.spm_h[i].sort()
                if i > 0:
                    self.lkp_g.append(
                        graph.adj_matrix_multiply(self.lkp_g[i - 1], self.g)
                    )
                    self.lkp_h.append(
                        graph.adj_matrix_multiply(self.lkp_h[i - 1], self.h)
                    )
                else:
                    self.lkp_g.append(copy.deepcopy(g))
                    self.lkp_h.append(copy.deepcopy(h))
            for i in range(self.n):
                for j in range(self.n):
                    self.lkp_g[i][j].sort()
                    self.lkp_h[i][j].sort()
            self.out = False

        def is_soln(self, a, k, finished):
            for i in range(self.n):
                for j in range(self.n):
                    if g[i][j] != h[a[i + 1]][a[j + 1]]:
                        return False
            return True

        def process_soln(self, a, k, finished):
            self.out = True

        def construct_cands(self, a, k, finished):
            cands = []
            in_iso = [False for _ in range(self.n)]
            for i in range(1, k):
                in_iso[a[i]] = True

            for i in range(self.n):
                if not in_iso[i] and self.feasible(a, k, i):
                    cands.append(i)
            return cands

        def feasible(self, a, k, i):
            if self.deg_g[k - 1] != self.deg_h[i]:
                return False
            if self.spm_g[k - 1] != self.spm_h[i]:
                return False
            for j in range(self.n):
                if self.lkp_g[j][k - 1] != self.lkp_h[j][i]:
                    return False
            return True

    if len(g) != len(h):
        return False

    a = [0] * (len(g) + 1)
    finished = [False]
    s = GraphIsomorphismSolver(g, h)
    backtrack(a, 0, finished, s)
    return s.out


# end snippet graph-isomorphism
