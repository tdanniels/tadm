"""UVA Judge 100"""

import functools
import sys


@functools.cache
def collatz(n):
    if n == 1:
        return 1
    if n % 2 == 1:
        n = 3 * n + 1
    else:
        n = n // 2

    i = 1 + collatz(n)

    return i


def solve(i: int, j: int):
    max_cyc = 0
    for k in range(min(i, j), max(i, j) + 1):
        max_cyc = max(max_cyc, collatz(k))
    return "{} {} {}".format(i, j, max_cyc)


def main():
    for line in sys.stdin:
        i, j = map(int, line.split())
        print(solve(i, j))


if __name__ == "__main__":
    main()
