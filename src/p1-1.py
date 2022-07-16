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
    i, j = min(i, j), max(i, j)
    for k in range(i, j + 1):
        max_cyc = max(max_cyc, collatz(k))
    return "{} {} {}".format(i, j, max_cyc)


def input():
    for line in map(str.rstrip, sys.stdin):
        print(solve(*map(int, line.split(" "))))


if __name__ == "__main__":
    input()
