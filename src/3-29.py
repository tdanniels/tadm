from collections import Counter, defaultdict
from typing import Tuple


# start snippet max-bigram
def max_bigram(corpus: str) -> Tuple[str, str, int]:
    table = defaultdict(Counter)
    l = list(corpus.split())
    maxpair = ("", "")
    maxpair_ct = 0
    for i, s in enumerate(l):
        if not s.isalpha():
            continue
        s = s.lower()
        try:
            table[s][l[i + 1]] += 1
            if (c := table[s][l[i + 1]]) > maxpair_ct:
                maxpair = (s, l[i + 1])
                maxpair_ct = c
        except IndexError:
            pass
    return (*maxpair, maxpair_ct)
    # end snippet max-bigram
