#!/usr/bin/env python3
# https://adventofcode.com/2025/day/1

from aoc_utils import load_real_input


def spinWheel(position, moves):
    counter = 0

    for line in moves:
        direction = line[0]
        distance = int(line[1:])

        prevPos = position
        if direction == "L":
            position -= distance
        elif direction == "R":
            position += distance
        # print(f"{line} @ {prevPos} => {position}")

        # div, mod = divmod(position, 100)
        # position = mod
        # if div != 0:
        #     counter += abs(div)
        # if div == 0 and mod == 0:
        #     counter += 1

        while position > 99:
            position -= 100
            if position != 0:
                counter += 1
                # print(f"    over 99. {position=}, {counter}")
        while position < 0:
            position += 100
            if prevPos != 0:
                counter += 1
            prevPos = 1
            # print(f"    under 0. {position=}, {counter}")
        if position == 0:
            counter += 1
            # print(f"    landed on 0. {counter=}")
    return counter


testCases = [
    (50, ["R10"], 0, "scenario1"),
    (50, ["L10"], 0, "scenario2"),
    (50, ["R50"], 1, "scenario3"),
    (50, ["L50"], 1, "scenario4"),
    (50, ["R100"], 1, "scenario5"),
    (50, ["R150"], 2, "scenario6"),
    (50, ["L100"], 1, "scenario7"),
    (50, ["L150"], 2, "scenario8"),
    (0, ["R10"], 0, "scenario9"),
    (0, ["L10"], 0, "scenario10"),
    (0, ["R100"], 1, "scenario11"),
    (0, ["L100"], 1, "scenario12"),
    (0, ["R150"], 1, "scenario13"),
    (0, ["R200"], 2, "scenario14"),
    (0, ["L150"], 1, "scenario15"),
    (0, ["L200"], 2, "scenario16"),
]

for test in testCases:
    result = spinWheel(test[0], test[1])
    if result != test[2]:
        print(f"FAIL: {test[3]} expected {test[2]}, got {result}")


test_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

real_input = load_real_input(__file__)

print(spinWheel(50, test_input.splitlines()))
print(spinWheel(50, real_input.splitlines()))
