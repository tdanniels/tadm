import copy
import itertools
from math import inf
from typing import List, Tuple

import graph
from trie import Trie


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


# start snippet list-combinations
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


# end snippet list-combinations


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
        self.deg_g = [len(list(filter(None, g[i]))) for i in range(len(g))]
        self.deg_h = [len(list(filter(None, h[i]))) for i in range(len(h))]
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
            if in_subg[v] or self.deg_g[k - 1] > self.deg_h[v]:
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


# start snippet bandwidth-reduction
def alternating_backtrack(a, k, finished, solver):
    if solver.is_soln(a, k, finished):
        solver.process_soln(a, k, finished)
    else:
        k += 1
        cands = solver.construct_cands(a, k, finished)
        for cand in cands:
            a[next_alternating_k(k, len(a))] = cand
            solver.make_move(a, k, finished)
            alternating_backtrack(a, k, finished, solver)
            solver.unmake_move(a, k, finished)
            if finished[0]:
                return


def next_alternating_k(k, n) -> int:
    if k % 2:
        return 1 + k // 2
    else:
        return n - k // 2


class BandwidthReductionSolver(Solver):
    def __init__(self, g):
        # NOTE: g is in adjacency list form.
        # TODO: abstract over + clearly distinguish between adjacency list and
        # adjacency matrix forms in the combinatorial and graph modules.
        self.g = g
        self.n = len(g)
        self.p, self.out = self.heuristic()

    def is_soln(self, a, k, finished):
        return k == self.n

    def process_soln(self, a, k, finished):
        if (c := self.cost(a)) < self.out:
            self.p = a[1:]
            self.out = c

    def construct_cands(self, a, k, finished):
        cands = []
        in_a = [False for _ in range(self.n)]
        for i in range(1, k):
            ofs = next_alternating_k(i, self.n + 1)
            in_a[a[ofs]] = True
        for i in range(self.n):
            if not in_a[i]:
                aprime = a[:]
                aprime[next_alternating_k(k, len(a))] = i
                if self.cost(aprime) < self.out:
                    cands.append(i)
        return cands

    def unmake_move(self, a, k, finished):
        a[next_alternating_k(k, len(a))] = None

    def heuristic(self):
        gs = []
        gsc = inf
        for u in range(self.n):
            s = [u]
            ds, _ = graph.bfs_adj_list(self.g, u)
            for du in range(1, self.n):
                app = False
                for v, d in enumerate(ds):
                    if d == du:
                        s.append(v)
                        app = True
                if not app:
                    break
            # Sort vertices of equal distance from u based on their degree.
            i = 1
            j = 1
            dstart = ds[i]
            while j < len(s) - 1:
                j += 1
                if ds[j] > dstart or j == len(s) - 1:
                    s[i:j] = sorted(s[i:j], key=lambda x: len(self.g[x]))
                    i = j
                    dstart = ds[j]
            if (sc := self.cost(s)) < gsc:
                gs = s
                gsc = sc
        return gs, gsc

    def cost(self, a):
        inv = [None] * len(a)
        for i, v in enumerate(a):
            if v is not None:
                inv[v] = i
        maxcost = 0
        for u in range(len(a)):
            if inv[u] is None:
                continue
            for v in self.g[u]:
                if inv[v] is None:
                    continue
                maxcost = max(abs(inv[u] - inv[v]), maxcost)
        return maxcost


def bandwidth_reduction(g) -> int:
    a = [None] * (len(g) + 1)
    finished = [False]
    s = BandwidthReductionSolver(g)
    alternating_backtrack(a, 0, finished, s)
    return s.p, s.out


# end snippet bandwidth-reduction

# start snippet max-clique
class MaxCliqueSolver(Solver):
    def __init__(self, g):
        self.g = g
        self.gm = graph.unweighted_adj_list_to_matrix(g)
        self.n = len(g)
        self.out = False

    def is_soln(self, a, k, finished):
        return k == len(a) - 1

    def process_soln(self, a, k, finished):
        self.out = True
        finished[0] = True

    def construct_cands(self, a, k, finished):
        cands = []
        in_clique = [False for _ in range(self.n)]
        for i in range(1, k):
            in_clique[a[i]] = True

        for i in range(self.n):
            include = True
            if in_clique[i]:
                continue
            for j in a[1:k]:
                if not self.gm[i][j]:
                    include = False
                    break
            if include:
                cands.append(i)
        return cands


def max_clique(g) -> int:
    # NOTE: g is in adjacency list form.
    c = 0
    d = [len(e) for _, e in enumerate(g)]
    sd = sorted(d, reverse=True)
    for k in range(1, len(g) + 1):
        finished = [False]
        a = [None] * (k + 1)
        j = 0
        for i in range(len(sd)):
            if i >= k - 1 and sd[i] > j - 1:
                j = max(j, i)
        keep = [v for v in range(len(g)) if d[v] >= j]
        gprime = graph.filtered_adj_list(g, keep)
        s = MaxCliqueSolver(gprime)
        backtrack(a, 0, finished, s)
        if not s.out:
            break
        c = k
    return c


# end snippet max-clique

# start snippet edge-coloring
class EdgeColoringSolver(Solver):
    def __init__(self, g, gamma):
        self.g = g
        self.gamma = gamma
        self.edges = [(u, v) for u in range(len(self.g)) for v in g[u] if u < v]
        self.out = False

    def is_soln(self, a, k, finished):
        return k == len(a) - 1

    def process_soln(self, a, k, finished):
        self.out = True
        finished[0] = True

    def construct_cands(self, a, k, finished):
        cands = []
        color_available = [True for _ in range(self.gamma)]
        u, v = self.edges[k - 1]
        for i, (s, t) in enumerate(self.edges[:k]):
            if s == u or t == v:
                color_available[a[i + 1]] = False

        for color in range(self.gamma):
            if color_available[color]:
                cands.append(color)
        return cands


def edge_coloring(g) -> int:
    # NOTE: g is in adjacency list form and assumed to be undirected.
    d = [len(e) for _, e in enumerate(g)]
    num_edges = sum(d) // 2
    delta = max(d)
    for gamma in (delta, delta + 1):
        a = [0] * (num_edges + 1)
        finished = [False]
        s = EdgeColoringSolver(g, gamma)
        backtrack(a, 0, finished, s)
        if s.out:
            return gamma
    raise ValueError("Graph g must have chromatic index in {delta(g), delta(g) + 1}")


# end snippet edge-coloring

# start snippet set-cover
class SetCoverSolver(Solver):
    def __init__(self, ss, n):
        self.ss = ss
        self.n = n
        self.out = inf

    def is_soln(self, a, k, finished):
        covered = [False] * self.n
        for i in range(1, k + 1):
            for v in self.ss[a[i]]:
                covered[v] = True
        return all(covered)

    def process_soln(self, a, k, finished):
        print(a[1 : k + 1])
        if k < self.out:
            self.out = k

    def construct_cands(self, a, k, finished):
        cands = []
        if k < self.out:
            in_cover = [False] * len(self.ss)
            for s in a[1:k]:
                in_cover[s] = True

            for i in range(len(self.ss)):
                if i >= k - 1 and not in_cover[i]:
                    cands.append(i)
        return cands


def set_cover(ss, n) -> int:
    a = [None] * (len(ss) + 1)
    finished = [False]

    # Eliminate strict subsets
    sss = [set(s) for s in ss]
    ss2 = []
    for i in range(len(sss)):
        include = True
        for j in range(len(sss)):
            if i != j and sss[i].issubset(sss[j]):
                include = False
                break
        if include:
            ss2.append(ss[i])

    s = SetCoverSolver(ss2, n)
    backtrack(a, 0, finished, s)
    return s.out


# end snippet set-cover

# start snippet keypad-words
class KeypadWordsSolver(Solver):
    digit2chars = {
        1: ["_", ",", "@"],
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"],
        0: [" "],
    }

    def __init__(self, digit_seq, wordtrie):
        self.digit_seq = digit_seq
        self.wordtrie = wordtrie
        self.n = len(digit_seq)
        self.out = []

    def is_soln(self, a, k, finished):
        return k == self.n and self.wordtrie.is_leaf(a[1 : k + 1])

    def process_soln(self, a, k, finished):
        self.out.append("".join(a[1:]))

    def construct_cands(self, a, k, finished):
        cands = []
        if k <= len(self.digit_seq):
            for c in self.digit2chars[self.digit_seq[k - 1]]:
                new_prefix = a[1:k]
                new_prefix.append(c)
                if new_prefix in self.wordtrie:
                    cands.append(c)
        return cands


def keypad_words(digit_seq: [int], dictionary: [str]) -> [str]:
    a = ["."] * (len(digit_seq) + 1)
    finished = [False]
    t = Trie(dictionary)
    s = KeypadWordsSolver(digit_seq, t)
    backtrack(a, 0, finished, s)
    return s.out


# end snippet keypad-words

# start snippet cnf-sat
class CnfSatSolver(Solver):
    def __init__(self, n, clauses):
        self.n = n
        self.out = False

        # Check for variables that are never / always negated.
        never_negated = [True] * (n + 1)
        always_negated = [True] * (n + 1)
        for i in range(1, n + 1):
            for c in clauses:
                if i in c:
                    always_negated[i] = False
                elif -i in c:
                    never_negated[i] = False

        # Appropriately fix variables that are never / always negated.
        self.fixed = [None] * (n + 1)
        for i in range(1, n + 1):
            if never_negated[i]:
                self.fixed[i] = True
            elif always_negated[i]:
                self.fixed[i] = False

        # Remove clauses with never / always negated variables.
        fclauses = []
        for c in clauses:
            add = True
            for l in c:
                if self.fixed[abs(l)] is not None:
                    add = False
                    break
            if add:
                fclauses.append(c[:])

        # Remove single variable clauses.
        sfclauses = []
        for c in fclauses:
            if len(c) == 1:
                self.fixed[c[0]] = c[0] > 0
            else:
                sfclauses.append(c[:])

        # Remove clauses with non-negated variables that are fixed to True, and
        # clauses with negated variables that are fixed to False. Otherwise remove
        # fixed variables from clauses that contain them.
        xclauses = []
        for c in fclauses:
            add_clause = True
            add_var = [True] * (len(c) + 1)
            for l in c:
                if l > 0 and self.fixed[l] or l < 0 and self.fixed[-l] == False:
                    add_clause = False
                    break
                if l < 0 and self.fixed[-l] or l > 0 and self.fixed[l] == False:
                    add_var[abs(l)] = False
            if add:
                clause = [v for i, v in enumerate(c) if add_var[i]]
                xclauses.append(clause)

        self.clauses = xclauses

    def is_soln(self, a, k, finished):
        for c in self.clauses:
            cs = False
            for l in c:
                if (l > 0 and a[l]) or (l < 0 and not a[-l]):
                    cs = True
                    break
            if not cs:
                return False
        return True

    def process_soln(self, a, k, finished):
        self.out = True
        finished[0] = True

    def construct_cands(self, a, k, finished):
        if k <= self.n:
            if self.fixed[k] is not None:
                return (self.fixed[k],)
            else:
                return (True, False)
        else:
            return tuple()


def cnf_sat(n, clauses):
    """
    Solve CNF-SAT instances.

    `n` is the number of variables (literals).

    `clauses` is of the form [[1, 2, -3], [-2, 3, -4]], which corresponds
    to the CNF-SAT instance (x_1, x_2, ~x_3) (~x_2, x_3, ~x_4).

    Note that literals are indexed from 1 and thus the literals in `clauses`
    must not be zero.
    """
    a = [False] * (n + 1)
    finished = [False]
    s = CnfSatSolver(n, clauses)
    backtrack(a, 0, finished, s)
    return s.out


# end snippet cnf-sat
