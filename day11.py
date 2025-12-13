#!/usr/bin/env python3
# https://adventofcode.com/2025/day/11

from aoc_utils import load_real_input

from heapq import heappop, heappush
from collections import defaultdict
from functools import cache

def q1(input):
    paths = {}
    for line in input:
        fr, to = line.split(":")
        to = to.split()
        paths[fr] = to

    work = [("you",)]
    all_paths = set()
    while work:
        path = heappop(work)
        node = path[-1]

        if node == "out":
            all_paths.add(path)

        for neighbour in paths.get(node, []):
            if neighbour in path:
                continue
            heappush(work, path + (neighbour,))

    return len(all_paths)

# FORWARDS
# svr -> dac? DOESN'T MATTER
# svr -> fft? SLOW
# fft -> dac ? SLOW
# dac -> fft ? SLOW
# dac -> fft? 0
# dac -> OUT? 3263

# BACKWARDS
# dac -> OUT? 3263
# dac -> fft? SLOW
# fft -> svr? 12371


# find routes from fft to dac and dac to svr, multiply (and by 3263)

def q2_dijkstra(input):
    paths = {}
    reverse_paths = defaultdict(list)
    for line in input:
        fr, to = line.split(":")
        to = to.split()
        paths[fr] = to
        for t in to:
            reverse_paths[t].append(fr)

    work = [("fft",)]
    all_paths = 0
    while work:
        path = heappop(work)
        node = path[-1]

        if node == "dac":
            # if "dac" in path and "fft" in path:
            all_paths += 1
            continue

        for neighbour in paths.get(node, []):
            if neighbour in path:
                continue
            if neighbour in ("svr", "out"):
                continue
            heappush(work, path + (neighbour,))

    return all_paths


paths = None
def q2(input):
    global paths
    paths = {}
    for line in input:
        fr, to = line.split(":")
        to = to.split()
        paths[fr] = to

    return num_of_paths("svr", False, False)


@cache
def num_of_paths(curr, visited_fft, visited_dac):
    if curr == "out":
        if visited_dac and visited_fft:
            return 1
        else:
            return 0

    if curr == "dac":
        visited_dac = True
    elif curr == "fft":
        visited_fft = True

    total = 0
    for neighbour in paths.get(curr, []):
        total += num_of_paths(neighbour, visited_fft, visited_dac)
    return total


sample_data = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""


real_data = load_real_input(__file__)

sample_data_2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""


print(q1(sample_data.splitlines()))
print(q1(real_data.splitlines()))

# print(q2(sample_data_2.splitlines()))
print(q2(real_data.splitlines()))
