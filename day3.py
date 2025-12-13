#!/usr/bin/env python3
# https://adventofcode.com/2025/day/3

from aoc_utils import load_real_input

def q1(banks):
    total = 0
    for bank in banks:
        joltage = ""
        highest = bank[0]
        highestPos = 0
        for pos, battery in enumerate(bank[:-1]):
            if battery > highest:
                highest = battery
                highestPos = pos
            if battery == 9:
                break
        joltage += str(highest)
        # print(f"{bank=} {highest=} {highestPos=}")
        highest = bank[highestPos+1]
        for battery in bank[highestPos+1:]:
            if battery > highest:
                highest = battery
            if battery == 9:
                break
        joltage += str(highest)
        # print(f"  {joltage=}")
        total += int(joltage)
    return total


def q2(banks):
    total = 0
    for bank in banks:
        joltage = ""
        highestPos = -1
        for digit in range(12):
            highest = -1
            for pos in range(highestPos+1, len(bank) - (12-digit) + 1):
                battery = int(bank[pos])
                if battery > highest:
                    highest = battery
                    highestPos = pos
                if battery == 9:
                    break
            joltage += str(highest)
            # print(f"{bank=} {highest=} {highestPos=} {joltage=}")
        total += int(joltage)
    return total


sample_input = """987654321111111
811111111111119
234234234234278
818181911112111"""


real_input = load_real_input(__file__)


print(q1(sample_input.splitlines()))
print(q1(real_input.splitlines()))

print(q2(sample_input.splitlines()))
print(q2(real_input.splitlines()))
