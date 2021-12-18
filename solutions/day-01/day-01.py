#!/usr/bin/env python3

def solve_part1(data):
    increment = 0
    previous = data[0]
    for x in data[1:]:
        if x > previous:
            increment += 1
        previous = x
    return increment


def solve_part2(data):
    increment = 0
    for y in range(len(data) - 3):
        if data[y + 3] > data[y]:
            increment += 1
    return increment

data = ""
with open("day-01-input.txt") as file: 
    data = file.read().splitlines() 

part1 = solve_part1(data)
print("Part 1: {}".format(part1))

part2 = solve_part2(data)
print("Part 2: {}".format(part2))
