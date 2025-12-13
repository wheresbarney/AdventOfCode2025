#!/usr/bin/env python3
# https://adventofcode.com/2025/day/7

from aoc_utils import load_real_input


from re import finditer
from functools import lru_cache


def q1(input):
    count = 0
    beams = {input[0].index("S"): True}
    for line in input[1:]:
        for m in finditer(r"\^", line):
            if beams[m.start()]:
                count += 1
                beams[m.start()] = False
                if m.start() < len(line):
                    beams[m.start() + 1] = True
                if m.start() >= 0:
                    beams[m.start() - 1] = True
    return count


def q2(input):
    return paths_to_end(tuple(input), 0, input[0].index("S"))

@lru_cache(maxsize=None)
def paths_to_end(plan, row, col):
    if row == len(plan):
        return 1
    if plan[row][col] != "^":
        return paths_to_end(plan, row + 1, col)
    return paths_to_end(plan, row + 1, col - 1) + paths_to_end(plan, row + 1, col + 1)


sample_input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^."""


real_input = load_real_input(__file__)


print(q1(sample_input.splitlines()))
print(q1(real_input.splitlines()))

print(q2(sample_input.splitlines()))
print(q2(real_input.splitlines()))
