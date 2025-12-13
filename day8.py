#!/usr/bin/env python3
# https://adventofcode.com/2025/day/8

from aoc_utils import load_real_input


from math import sqrt, prod


def q1(input):
    jboxes = [[int(n) for n in l.split(",")] for l in input]

    distances = []
    for i, jbox in enumerate(jboxes):
        for j, jbox2 in enumerate(jboxes[i+1:]):
            distance = sqrt((jbox[0] - jbox2[0])**2 + (jbox[1] - jbox2[1])**2 + (jbox[2] - jbox2[2])**2)
            distances.append((distance, i, j+i+1))

    max_distances = 10 if len(input) == 20 else 1000
    nearest = [(i, j) for _, i, j in sorted(distances)][:max_distances]

    circuits = [{n} for n in range(len(jboxes))]
    for i, j in nearest:
        matched_circuit = None
        for n, circuit in enumerate(circuits):
            if i in circuit or j in circuit:
                if matched_circuit is None:
                    matched_circuit = circuit
                else:
                    matched_circuit.update(circuit)
                    del circuits[n]
                    break
    return prod([len(c) for c in sorted(circuits, key=len, reverse=True)[:3]])

def q2(input):
    jboxes = [[int(n) for n in l.split(",")] for l in input]

    distances = []
    for i, jbox in enumerate(jboxes):
        for j, jbox2 in enumerate(jboxes[i+1:]):
            distance = sqrt((jbox[0] - jbox2[0])**2 + (jbox[1] - jbox2[1])**2 + (jbox[2] - jbox2[2])**2)
            distances.append((distance, i, j+i+1))

    nearest = [(i, j) for _, i, j in sorted(distances)]

    circuits = [{n} for n in range(len(jboxes))]
    for i, j in nearest:
        matched_circuit = None
        for n, circuit in enumerate(circuits):
            if i in circuit or j in circuit:
                if matched_circuit is None:
                    matched_circuit = circuit
                else:
                    matched_circuit.update(circuit)
                    del circuits[n]
                    if len(circuits) == 1:
                        return jboxes[i][0] * jboxes[j][0]
                    break



sample_input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


real_input = load_real_input(__file__)


print(q1(sample_input.splitlines()))
print(q1(real_input.splitlines()))

print(q2(sample_input.splitlines()))
print(q2(real_input.splitlines()))
