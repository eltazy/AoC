# https://adventofcode.com/2022/day/3

def intersect(sack):
    return list(set(sack[0]).intersection(set(sack[1])))[0]


def char_pos(c):
    i = ord(c)
    if i < 91:
        return i-64+26
    return i-96


def get_badge(gr):
    return list(set(gr[0]).intersection(set(gr[1])).intersection(set(gr[2])))[0]


file = open('input.txt', 'r')
# file = open('sample.txt', 'r')
raw_input = file.read().splitlines()

# Part I solution
input1 = [[l[:len(l)//2], l[len(l)//2:]] for l in raw_input]
input1 = [intersect(sack) for sack in input1]
input1 = [char_pos(c) for c in input1]
out1 = sum(input1)
print('1. What is the sum of the priorities of those item types? => ', out1)
# End part I

# Your puzzle answer was 7850.

# Part II solution
groups = []
temp = [raw_input[0]]
for i in range(1, len(raw_input)):
    if i % 3:
        temp.append(raw_input[i])
    else:
        groups.append(temp)
        temp = [raw_input[i]]
groups.append(temp)
groups = [char_pos(get_badge(g)) for g in groups]
out2 = sum(groups)
print("2. What is the sum of the priorities of those item types? => ", out2)


# End part II

# Your puzzle answer was 2581.
