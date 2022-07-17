"""UVA Judge 10142"""

from collections import deque
from dataclasses import dataclass
import sys


@dataclass
class Vote:
    candidates: list[str]
    ballots: list[deque[int]]


def lowest_vote_count(pile, eliminated):
    return len(
        min(
            map(
                lambda x: x[1],
                filter(lambda x: x[0] not in eliminated, enumerate(pile)),
            ),
            key=len,
        )
    )


def solve_inner(vote: Vote):
    eliminated = set()
    nballots = len(vote.ballots)
    # pile[i] = a list of ballots that currently rank candidate i first.
    pile = [[] for _ in range(len(vote.candidates))]
    for b in vote.ballots:
        pile[b[0]].append(b)

    while True:
        for i, p in enumerate(pile):
            if len(p) > nballots / 2:
                return [vote.candidates[i]]
        # No winner yet. Move the lowest ranked candidates' ballots
        # to the ballots' next choices and eliminate the losers (!).
        lvc = lowest_vote_count(pile, eliminated)
        # All tied?
        if all(
            map(
                lambda p: len(p[1]) == lvc,
                filter(lambda i: i[0] not in eliminated, enumerate(pile)),
            )
        ):
            return [
                vote.candidates[i]
                for i, _ in enumerate(vote.candidates)
                if i not in eliminated
            ]
        for i, p in filter(lambda i: i[0] not in eliminated, enumerate(pile)):
            if len(p) == lvc:
                eliminated.add(i)
        # Copy ballots from losers.
        for i, p in filter(lambda i: i[0] in eliminated, enumerate(pile)):
            for b in p:
                while b[0] in eliminated:
                    b.popleft()
                if len(b) > 0:
                    pile[b[0]].append(b)
        # Delete losers' ballots.
        for l in eliminated:
            pile[l].clear()


def solve(votes) -> list[str]:
    output = []
    for i, vote in enumerate(votes):
        if i > 0:
            output.append("")
        output.extend(solve_inner(vote))
    return output


def parse(lines: deque[str]) -> list[Vote]:
    votes = []
    cases = int(lines.popleft())
    _ = lines.popleft()
    while cases > 0:
        candidates = []
        ballots = []
        n_candidates = int(lines.popleft())
        for _ in range(n_candidates):
            candidates.append(lines.popleft())
        while len(lines) > 0:
            ballot = lines.popleft()
            if ballot == "":
                break
            ballots.append(deque(map(lambda x: int(x) - 1, ballot.split())))
        votes.append(Vote(candidates, ballots))
        cases -= 1
    return votes


def main():
    lines = deque()
    for line in map(str.rstrip, sys.stdin):
        lines.append(line)
    print("\n".join(solve(parse(lines))))


if __name__ == "__main__":
    main()
