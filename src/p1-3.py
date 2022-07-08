from collections import deque
from dataclasses import dataclass
import sys


@dataclass
class Vote:
    candidates: list[str]
    ballots: list[list[int]]


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
    output = []
    eliminated = []
    # pile[i] = a list of ballots that currently rank candidate i first.
    pile = [[] for _ in range(len(vote.candidates))]
    for b in vote.ballots:
        pile[b[0]].append(b)

    while True:
        for i, p in enumerate(pile):
            if len(p) > len(vote.candidates) / 2:
                output.append(vote.candidates[i])
                return output
        # No winner yet. Move the lowest ranked candidates' ballots
        # to the ballots' next choices and eliminate the losers (!).
        lvc = lowest_vote_count(pile, eliminated)
        for i, p in enumerate(pile):
            if len(p) == lvc:
                eliminated.append(i)
        if len(eliminated) == len(vote.candidates):
            output.extend(vote.candidates)
            return output
        # Copy ballots from losers.
        for i, p in enumerate(pile):
            if i in eliminated:
                for b in p:
                    while b[0] in eliminated:
                        b = b[1:]
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
            ballots.append(list(map(lambda x: int(x) - 1, ballot.split(" "))))
        votes.append(Vote(candidates, ballots))
        cases -= 1
    return votes


# For online judge.
def input():
    lines = deque()
    for line in map(str.rstrip, sys.stdin):
        lines.append(line)
    print("\n".join(solve(parse(lines))))


# For local testing.
if __name__ == "__main__":
    inp = deque(
        [
            "1",
            "",
            "3",
            "John Doe",
            "Jane Smith",
            "Sirhan Sirhan",
            "1 2 3",
            "2 1 3",
            "2 3 1",
            "1 2 3",
            "3 1 2",
        ]
    )
    assert solve(parse(inp)) == ["John Doe"]

    inp = deque(
        [
            "2",
            "",
            "3",
            "John Doe",
            "Jane Smith",
            "Sirhan Sirhan",
            "1 2 3",
            "2 1 3",
            "2 3 1",
            "1 2 3",
            "3 1 2",
            "",
            "2",
            "a",
            "b",
            "1 2",
            "2 1",
        ]
    )
    assert solve(parse(inp)) == ["John Doe", "", "a", "b"]
