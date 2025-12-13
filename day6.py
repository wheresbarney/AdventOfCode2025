#!/usr/bin/env python3
# https://adventofcode.com/2025/day/6

from aoc_utils import load_real_input

from math import prod
import re

def q1(input):
    columns = [[int(n)] for n in input[0].split()]
    for line in input[1:-1]:
        for i, n in enumerate([int(n) for n in line.split()]):
            columns[i].append(n)

    total = 0
    for op, vals in zip(input[-1].split(), columns):
        if op == "*":
            total += prod(vals)
        elif op == "+":
            total += sum(vals)
    return total


def q2(input):
    total = 0
    op_indices = [m.start() for m in re.finditer(r"[\+\*]", input[-1])]
    for i, col_start in enumerate(op_indices):
        if col_start >= len(input[0]):
            break
        vals = []
        col_end = op_indices[i + 1] - 1 if i < len(op_indices) - 1 else len(input[0])
        for line in input[:-1]:
            vals.append(line[col_start:col_end])
        nums = []
        for n in range(len(vals[0])):
            nums.append(int("".join([val[n] for val in vals])))
        if input[-1][col_start] == "*":
            # print(f"[{col_start},{col_end}]: multiplying {nums} = {prod(nums)}")
            total += prod(nums)
        else:
            # print(f"[{col_start},{col_end}]: adding {nums} = {sum(nums)}")
            total += sum(nums)
    return total








sample_input = [\
"123 328  51 64 ",
" 45 64  387 23 ",
"  6 98  215 314",
"*   +   *   +  "]

real_input = load_real_input(__file__).splitlines()

print(q1(sample_input))
print(q1(real_input))

print(q2(sample_input))
print(q2(real_input))
