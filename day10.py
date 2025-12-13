#!/usr/bin/env python3
# https://adventofcode.com/2025/day/10

from aoc_utils import load_real_input

from re import findall
from itertools import combinations
import numpy as np
from scipy.optimize import linprog

def q1(schematics):
    total_presses = 0
    for schematic in schematics:
        target_str = schematic[1:schematic.find("]")]
        target = int(target_str.replace(".", "0").replace("#", "1"), base=2)
        buttons = [[int(n) for n in s.split(",")] for s in findall(r"\(([\d,]+)\)", schematic)]
        buttons = [int("".join(["1" if n in b else "0" for n in range(len(target_str))]), base=2) for b in buttons]
        # print(f"mapped {schematic} to {target}, {buttons}")

        presses = None
        for n in range(0, len(target_str)):
            for c in combinations(buttons, n+1):
                if target == columnwise_binary_addition(c, len(target_str)):
                    # print(f"{target=} made with {n+1} presses: {c}")
                    presses = n+1
                    break
            if presses:
                total_presses += presses
                break
        if not presses:
            raise Exception(f"no combos found for {schematic}")

    return total_presses


def columnwise_binary_addition(vals, bits):
    binary_res = []
    binary_strs = [bin(v).removeprefix("0b").zfill(bits) for v in vals]
    for i in range(bits):
        binary_res.append(str(sum([int(s[i]) for s in binary_strs]) % 2))
    # print(f"  adding {vals} ({bits=}) as {binary_strs} => {"".join(binary_res)} => {int("".join(binary_res), base=2)}")
    return int("".join(binary_res), base=2)


# from https://github.com/jad2192/advent_of_code_2025/blob/main/aoc2025/day10.py
def q2(schematics):
    total = 0
    for schematic in schematics:
        target_str = schematic[1:schematic.find("]")]
        buttons = [[int(n) for n in s.split(",")] for s in findall(r"\(([\d,]+)\)", schematic)]
        buttons = [[1 if n in b else 0 for n in range(len(target_str))] for b in buttons]
        joltage = [int(j) for j in schematic[schematic.find("{")+1:-1].split(",")]

        optimizer_c = [1] * len(buttons)
        total += linprog(c=optimizer_c, A_eq=np.array(buttons).T, b_eq=joltage, integrality=optimizer_c).fun
    return total


sample_data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


real_data = load_real_input(__file__)


print(q1(sample_data.splitlines()))
print(q1(real_data.splitlines()))

print(q2(sample_data.splitlines()))
print(q2(real_data.splitlines()))
