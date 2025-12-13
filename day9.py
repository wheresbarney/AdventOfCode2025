#!/usr/bin/env python3
# https://adventofcode.com/2025/day/9

from aoc_utils import load_real_input


from functools import lru_cache
from collections import deque


def q1(coords):
    coords = [tuple(int(n) for n in line.split(",")) for line in coords]
    max_area = 0
    for i, p1 in enumerate(coords):
        for p2 in coords[i + 1 :]:
            area = abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1)
            if area > max_area:
                max_area = area
    return max_area


lobound = hibound = edges = None
def q2_doesnt_work_written_by_me(coords):
    coords = [tuple(int(n) for n in line.split(",")) for line in coords]

    rects = []
    for i, p1 in enumerate(coords):
        for p2 in coords[i + 1 :]:
            tl = min(p1[0], p2[0]), min(p1[1], p2[1])
            br = max(p1[0], p2[0]), max(p1[1], p2[1])
            rects.append(((br[0] - tl[0] + 1) * (br[1] - tl[1] + 1), tl, br))
    rects = sorted(rects)

    # define largest rectangle that bounds the pattern — any path to any edge means the start point is not inside the pattern
    # build set of edges — left/right and up/down
    # for each possible rectangle, take a random point inside and see if there is any path to any edge. If so, add all points on that path to a set 'outside'
    # before calculating the path to outside, see if there are any points in the set 'outside' that are inside the rectangle. If so, the rectangle fails
    global lobound; lobound = min([p[0] for p in coords]), min([p[1] for p in coords])
    global hibound; hibound = max([p[0] for p in coords]), max([p[1] for p in coords])
    global edges; edges = []
    for i, p1 in enumerate(coords):
        if i == len(coords) - 1:
            p2 = coords[0]
        else:
            p2 = coords[i + 1]
        edges.append((p1, p2))
    edges = tuple(edges)

    # binary search through rectangles, test each contained square (memoized)
    mn, mx = 0, len(rects) - 1 # mn always good, mx always bad
    if red_green(rects[mx][1], rects[mx][2]):
        return rects[mx][0]
    if not red_green(rects[0][1], rects[0][2]):
        raise Exception("none are good")

    while True:
        i = mn + (mx - mn) // 2
        tl, br = rects[i][1], rects[i][2]
        print(f"binary search {tl}-{br} @{i} between {mn}-{mx}")
        good = red_green(tl, br)

        if good:
            mn = i
        else:
            mx = i

        if mx == mn + 1:
            print(f"  binary search completed @{mn} => {rects[mn]} ({mn=}, {mx=})")
            return rects[mn][0]


known_paths_to_any_edge = set()
def red_green(tl, br):
    if any(tl[0] <= p[0] <= br[0] and tl[1] <= p[1] <= br[1] for p in known_paths_to_any_edge):
        # print(f"rejecting {tl}-{br}, matches known_paths_to_any_edge ({len(known_paths_to_any_edge)})")
        return False

    q = deque()
    q.append((tl[0]+1, tl[1]+1))
    return path_to_edge(q, [q[0]])


def path_to_edge(q, path):
    while q:
        p = q.popleft()

        if p in known_paths_to_any_edge:
            print(f"  rejecting {p}, matches known_paths_to_edge")
            known_paths_to_any_edge.update(path)
            return True

        # if it's on an edge, no!
        if on_edge(p):
            continue

        # if it's on the bounds, yes!
        if p[0] == lobound[0] or p[0] == hibound[0] or p[1] == lobound[1] or p[1] == hibound[1]:
            print(f"  rejecting {p}, hit bounds")
            known_paths_to_any_edge.update(path)
            return True

        # otherwise, recurse left, right, up, down
        q.append((p[0]-1, p[1]))
        q.append((p[0]+1, p[1]))
        q.append((p[0], p[1]-1))
        q.append((p[0], p[1]+1))
    return False


def on_edge(p):
    return any(
        (
            p[0] == edge[0][0] and (edge[0][1] <= p[1] <= edge[1][1])
        ) or (
            p[1] == edge[0][1] and (edge[0][0] <= p[0] <= edge[1][0])
        ) for edge in edges)


# https://www.reddit.com/r/adventofcode/comments/1phywvn/comment/nt995wd/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
def q2(coords):
    corners = [tuple(map(int, line.split(","))) for line in coords]

    n = len(corners)

    def get_size(x1, y1, x2, y2):
        x = abs(x1 - x2) + 1
        y = abs(y1 - y2) + 1
        return x * y

    edges = []
    sizes = []
    for i in range(n):
        edges.append(sorted((corners[i], corners[i-1])))
        for j in range(i+1, n):
            c1, c2 = sorted((corners[i], corners[j]))
            sizes.append((get_size(*c1, *c2), c1, c2))

    edges.sort(reverse=True, key=lambda e: get_size(*e[0], *e[1]))
    sizes.sort(reverse=True)

    for size, (x1, y1), (x2, y2) in sizes:
        y1, y2 = sorted((y1, y2))
        if not any(
            (x4 > x1 and x3 < x2 and y4 > y1 and y3 < y2)
            for (x3, y3), (x4, y4) in edges
        ):
            return size


sample_input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""


real_input = load_real_input(__file__)


print(q1(sample_input.splitlines()))
print(q1(real_input.splitlines()))

print(q2(sample_input.splitlines()))
print(q2(real_input.splitlines()))
