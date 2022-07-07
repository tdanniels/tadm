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
        z = len(list(filter(lambda x: x == 0, combs.values())))
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


if __name__ == "__main__":
    S = [1, 2, 3, 4, 5]
    k = 3
    l = 2
    assert check_tickets([[1, 2, 3], [1, 4, 5]], S, k, l)
    assert not check_tickets([[1, 2, 3], [1, 2, 4]], S, k, l)

    gen = gen_tickets(S, k, l)
    assert check_tickets(gen, S, k, l)
    assert len(gen) == 2

    S = list(range(1, 11))
    k = 6
    l = 3
    gen = gen_tickets(S, k, l)
    assert check_tickets(gen, S, k, l)

    S = list(range(1, 16))
    k = 6
    l = 3
    assert check_tickets(
        [
            [2, 4, 8, 10, 13, 14],
            [4, 5, 7, 8, 12, 15],
            [1, 2, 3, 6, 11, 13],
            [3, 5, 6, 9, 10, 15],
            [1, 7, 9, 11, 12, 14],
        ],
        S,
        k,
        l,
    )
    assert not check_tickets(
        [
            [2, 4, 8, 10, 13, 14],
            [4, 5, 7, 8, 12, 15],
            [1, 2, 3, 6, 11, 13],
            [3, 5, 6, 9, 10, 15],
        ],
        S,
        k,
        l,
    )
