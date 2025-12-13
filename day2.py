#!/usr/bin/env python3
# https://adventofcode.com/2025/day/2

from aoc_utils import load_real_input


def parse(input):
    input = [r.split("-") for r in input.split(",")]
    return [[int(r[0]), int(r[1])] for r in input]


def q1(input):
    total = 0
    ranges = parse(input)
    for r in ranges:
        for n in range(r[0], r[1] + 1):
            s = str(n)
            l = len(s)
            if l % 2 != 0:
                continue
            if s[: l // 2] == s[l // 2 :]:
                total += n
    return total


def q2(input):
    total = 0
    ranges = parse(input)
    for r in ranges:
        for n in range(r[0], r[1] + 1):
            s = str(n)
            l = len(s)
            for i in range(l // 2):
                if s[: i + 1] * (l // (i + 1)) == s:
                    total += n
                    break
    return total


sample_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

real_input = load_real_input(__file__)

print(q1(sample_input))
print(q1(real_input))

print(q2(sample_input))
print(q2(real_input))
