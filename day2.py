#!/usr/bin/env python3
# https://adventofcode.com/2025/day/2


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

real_input = """975119-1004307,35171358-35313940,6258659887-6258804661,737649-837633,85745820-85956280,9627354-9679470,2327309144-2327509647,301168-351545,537261-631588,364281214-364453549,9563727253-9563879587,3680-9127,388369417-388406569,6677501-6752949,650804-678722,3314531-3365076,1052-2547,24134-68316,8888820274-8888998305,82614-107458,456819-529037,358216-389777,24222539-24266446,874565-916752,3886244-3960191,25-110,9696951376-9696996784,171-671,5656545867-5656605587,75795017-75865731,1-16,181025-232078"""

print(q1(sample_input))
print(q1(real_input))

print(q2(sample_input))
print(q2(real_input))
