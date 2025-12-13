#!/usr/bin/env python3
# https://adventofcode.com/2025/day/12

from aoc_utils import load_real_input


from copy import deepcopy
from functools import lru_cache


rotated_shapes = None

def q1(input):
    shapes = []
    trees = []
    current_shape = []
    for line in input:
        if line == "":
            shapes.append(current_shape)
            current_shape = []
            continue
        elif "x" in line:
            grid, present_counts = line.split(":")
            grid = [int(n) for n in grid.split("x")]
            present_counts = [int(p) for p in present_counts.split()]
            trees.append((grid, present_counts))
        elif ":" not in line:
            current_shape.append(line)

    global rotated_shapes
    rotated_shapes = []
    for shape in shapes:
        rots = [tuple(shape)]
        for _ in range(3):
            rots.append(tuple(zip(*reversed(rots[-1]))))
        rotated_shapes.append(rots)

    fits = 0
    for grid, present_counts in trees:
        layout = tuple([tuple([False] * grid[0]) for _ in range(grid[1])])
        presents = []

        total_present_area = 0
        for p, c in enumerate(present_counts):
            total_present_area += c * sum(s.count("#") for s in shapes[p])
            presents.extend([p] * c)

        # quick check, are presents just too big?
        if total_present_area > grid[0] * grid[1]:
            continue

        if fits_grid(layout, presents):
            fits += 1

    return fits


def fits_grid(layout, shapes):
    if not shapes:
        return True

    shape_index = shapes[-1]
    global rotated_shapes

    for y in range(len(layout)):
        for x in range(len(layout[y])):
            for rotation in range(4):
                shape = rotated_shapes[shape_index][rotation]
                new_layout = fits_shape(layout, shape, x, y)
                if not new_layout:
                    continue
                if fits_grid(new_layout, shapes[:-1]):
                    return True
    return False


# @lru_cache(maxsize=None)
def fits_shape(layout, shape, x, y):
    new_points = set()
    for sy, row in enumerate(shape):
        for sx, cell in enumerate(row):
            if cell == "#":
                nx = x + sx
                ny = y + sy
                if ny >= len(layout):
                    return None
                if nx >= len(layout[ny]):
                    return None
                if layout[ny][nx]:
                    return None
                new_points.add((nx, ny))

    return tuple([tuple([layout[y][x] or ((x, y) in new_points) for x in range(len(layout[y]))]) for y in range(len(layout))])


sample_data = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

real_data = load_real_input(__file__)

# print(q1(sample_data.splitlines()))
print(q1(real_data.splitlines()))
