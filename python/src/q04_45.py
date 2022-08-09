import heapq
from math import inf
from typing import Optional, Tuple


# start snippet closest3
def closest3(w1: list[int], w2: list[int], w3: list[int]) -> Optional[Tuple[int, int]]:
    for w in w1, w2, w3:
        if any(x < 0 for x in w):
            raise ValueError("Indices must be >= 0")

    q = list(
        heapq.merge(
            zip(w1, [0] * len(w1)),
            zip(w2, [1] * len(w2)),
            zip(w3, [2] * len(w3)),
        )
    )

    # I'd have preferred to initialize these to None, but Pyright was really
    # fighting me on that one.
    triple = [-1, -1, -1]
    out = None
    mindist = inf

    for v, i in q:
        triple[i] = v
        if -1 not in triple and (dist := max(triple) - min(triple)) < mindist:
            mindist = dist
            out = (min(triple), max(triple))
    return out
    # end snippet closest3
