# https://adventofcode.com/2022/day/1

file = open('input.txt', 'r')
# file = open('sample.txt', 'r')
input = file.read().splitlines()

# Part I solution
elves = []
temp = []
for i in input:
    if i:
        temp.append(int(i))
    else:
        elves.append(temp)
        temp = []
elves.append(temp)

elves_power = sorted([sum(arr) for arr in elves])
out = elves_power[-1]
print('1. How many total Calories is that Elf carrying? =>', out)
# End part I
# Your puzzle answer was 67633.

# Part II solution
out = sum(elves_power[-3:])
print('2. How many Calories are those Elves carrying in total? =>', out)
# End part II
# Your puzzle answer was 199628.
