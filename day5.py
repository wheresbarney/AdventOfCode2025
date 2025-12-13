#!/usr/bin/env python3
# https://adventofcode.com/2025/day/5

from aoc_utils import load_real_input

from collections import deque


def q1(input):
    fresh_ranges = []
    fresh_total = 0
    for line in input:
        if "-" in line:
            fresh_ranges.append([int(n) for n in line.split("-")])
        elif line != "":
            ingredient = int(line)
            for mn, mx in fresh_ranges:
                if ingredient >= mn and ingredient <= mx:
                    fresh_total += 1
                    break
    return fresh_total


def q2(input):
    fresh_ranges = []
    for line in input:
        if "-" in line:
            fresh_ranges.append([int(n) for n in line.split("-")])
        else:
            break

    merged_ranges = []
    queue = deque(fresh_ranges)
    while queue:
        new_range = queue.popleft()
        unique = True
        for existing_range in merged_ranges:
            modified_range = []
            if new_range[0] < existing_range[0] and new_range[1] >= existing_range[0]:
                modified_range.append([new_range[0], existing_range[0]-1])
            if new_range[1] > existing_range[1] and new_range[0] <= existing_range[1]:
                modified_range.append([existing_range[1]+1, new_range[1]])
            if modified_range:
                queue.extend(modified_range)
                unique = False
                break

            if new_range[0] >= existing_range[0] and new_range[1] <= existing_range[1]:
                unique = False
        if unique:
            merged_ranges.append(new_range)
    return sum([r[1]-r[0]+1 for r in merged_ranges])


sample_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

real_input = load_real_input(__file__)

print(q1(sample_input.splitlines()))
print(q1(real_input.splitlines()))

print(q2(sample_input.splitlines()))
print(q2(real_input.splitlines()))
