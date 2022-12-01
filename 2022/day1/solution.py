# https://adventofcode.com/2022/day/1

file = open('input.txt', 'r')
# file = open('sample.txt', 'r')
input = file.read().splitlines()

# Part I solution
elves = []
temp = []
for i in input:
    if i: temp.append(int(i))
    else:
        elves.append(temp)
        temp=[]
elves.append(temp)
elves_power = [sum(arr) for arr in elves]
res1 = max(elves_power)
print('Find the Elf carrying the most Calories.\nHow many total Calories is that Elf carrying? => ', res1)
# End part I

# Your puzzle answer was 67633.

# Part II solution
elves_power.sort(reverse=True)
res2 = sum(elves_power[:3])
print('Find the top three Elves carrying the most Calories.\nHow many Calories are those Elves carrying in total? => ', res2)
# End part II

# Your puzzle answer was 199628.
