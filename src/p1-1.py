import functools
import sys


def collatz(n):
    i = 0
    while True:
        i += 1
        if n == 1:
            return i
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2


def solve(i, j):
    max_cyc = 0
    for k in range(i, j + 1):
        max_cyc = max(max_cyc, collatz(k))
    return "{} {} {}".format(i, j, max_cyc)


# For online judge.
def input():
    for line in map(str.rstrip, sys.stdin):
        print(solve(*map(int, line.split(" "))))


# For local testing.
if __name__ == "__main__":
    assert solve(1, 10) == "1 10 20"
    assert solve(100, 200) == "100 200 125"
    assert solve(201, 210) == "201 210 89"
    assert solve(900, 1000) == "900 1000 174"
    # Worst case input:
    assert solve(1, 9999) == "1 9999 262"
