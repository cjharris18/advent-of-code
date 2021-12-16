#!/usr/bin/env python3

data = ""
with open("day-02-input.txt") as file: 
    data = file.read().splitlines() 

def solve_part1(data): 
    forward = 0 
    depth = 0

    for commandInText in data:
        command = commandInText[:-2]
        move = int(commandInText[-1])

        if command == 'forward':
            forward += move
        elif command == 'down':
            depth += move
        elif command == 'up':
            depth -= move

    return (forward * depth)


def solve_part2(data): 
    forward = 0 
    depth = 0 
    aim = 0

    for commandInText in data:
        command = commandInText[:-2]
        move = int(commandInText[-1])

        if command == 'forward':
            forward += move
            depth += aim * move
        elif command == 'down':
            aim += move
        elif command == 'up':
            aim -= move
    
    return (forward * depth)

part1 = solve_part1(data)
print("Part 1: {}".format(part1))

part2 = solve_part2(data)
print("Part 2: {}".format(part2))
