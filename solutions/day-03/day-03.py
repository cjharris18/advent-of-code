#!/usr/bin/env python3

def solve_part1(data):

    gammaRate = "".join(["1" if col.count("1") > col.count("0") else "0" for col in [[l[i] for l in data] for i in range(len(data[0]))]])
    epsilonRate = int("".join(["1" if x == "0" else "0" for x in gammaRate]), 2)
    gammaRate = int(gammaRate,2)

    return gammaRate * epsilonRate

"""
For Part 2, I got a bit overwhelmed by all the requirements so I broke it down a lot more, to further understand it.
Hence, this solution is a LOT longer and probably not as nice code.
I also commented this far more thoroughly to understand it as I was developing it.
"""

# Just count the bits.
def count_bits(myArray, index):
    binaryZeroes = 0
    binaryOnes = 0

    for line in myArray:
        if line[index] == "0":
            binaryZeroes += 1
        if line[index] == "1":
            binaryOnes += 1
    return binaryZeroes, binaryOnes

# Find the Most common value. 
def most_common(binaryZeroes, binaryOnes):
    if binaryOnes >= binaryZeroes:
        return '1'
    else:
        return '0'

# Find the least common value.
def least_common(binaryZeroes, binaryOnes):
    if binaryOnes >= binaryZeroes:
        return '0'
    else:
        return '1'
 
"""
Search the list recursively.
We take the index and the mode, we call all the functions from this function.
"""
def recursive_search(myArray, index, mode):
    if len(myArray) == 1:
        return myArray[0]

    else:
        binaryZeroes, binaryOnes = count_bits(myArray, index)
        if mode == 'mostCommon':
            current_column = most_common(binaryZeroes, binaryOnes)
        elif mode == 'leastCommon':
            current_column = least_common(binaryZeroes, binaryOnes)
        
        myNewArray = []
        for item in myArray:
            if item[index] == current_column:
                myNewArray.append(item)
        index += 1

        return recursive_search(myNewArray, index, mode)

# Bring it all together so that we can format the answer nicely later.
def solve_part2(data):      
  return int(recursive_search(data,0, 'mostCommon'), 2) * int(recursive_search(data,0, 'leastCommon'), 2)

data = ""
with open("day-03-input.txt") as file: 
    data = file.read().splitlines() 

part1 = solve_part1(data)
print("Part 1: {}".format(part1))

part2 = solve_part2(data)
print("Part 2: {}".format(part2))