from itertools import combinations


# start snippet check-tickets
def check_tickets(T: list[list[int]], S: list[int], k: int, l: int) -> bool:
    Ss = set(S)
    Ts = set([frozenset(t) for t in T])
    for lsub in map(set, combinations(Ss, l)):
        # Check if our l-subset is explicitly covered.
        if any((lsub.issubset(t) for t in Ts)):
            continue
        # If it's not, we need to ensure that at least one l-subset of each of
        # the possible extensions of lsub are covered.
        for ext in map(set, combinations(Ss - lsub, k - l)):
            try:
                for t in Ts:
                    for vlsub in map(set, combinations(lsub.union(ext), l)):
                        if vlsub.issubset(t):
                            raise StopIteration
                return False
            except StopIteration:
                pass
    return True
    # end snippet check-tickets


# start snippet gen-tickets
def gen_tickets(S: list[int], k: int, l: int) -> list[list[int]]:
    Ss = set(S)
    T = []
    combs = {frozenset(c): 0 for c in combinations(S, l)}
    while 0 in combs.values():
        # Let's add a ticket that covers (perhaps indirectly) as many uncovered
        # l-subsets as possible.
        max_tcover = []
        max_ticket = None
        for ticket in map(set, combinations(S, k)):
            tcover = []
            Tt = [set(t) for t in T + [list(ticket)]]
            for lsub in {k for k, v in combs.items() if v == 0}:
                covered = True
                if lsub.issubset(ticket):
                    tcover.append(lsub)
                    continue
                for ext in map(set, combinations(Ss - lsub, k - l)):
                    try:
                        if not covered:
                            break
                        for t in Tt:
                            for vlsub in map(set, combinations(lsub.union(ext), l)):
                                if vlsub.issubset(t):
                                    raise StopIteration
                        covered = False
                    except StopIteration:
                        pass
                if covered:
                    tcover.append(lsub)
            if len(tcover) > len(max_tcover):
                max_tcover = tcover
                max_ticket = ticket
        assert max_ticket is not None
        T.append(list(max_ticket))
        for tc in max_tcover:
            combs[frozenset(tc)] = 1
    return T
    # end snippet gen-tickets
