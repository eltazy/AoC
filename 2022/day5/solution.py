# https://adventofcode.com/2022/day/5
from collections import deque

file = open('input.txt', 'r')
# file = open('sample.txt', 'r')
raw_input = file.read().splitlines()

# Part I solution
raw_input = [l.split(',') for l in raw_input]
sep = raw_input.index([''])
cargo, moves = [c[0] for c in raw_input[:sep]], [c[0] for c in raw_input[sep+1:]]

cols = int(cargo[-1].strip()[-1])
cargo, moves = cargo[:-1], [ m.split() for m in moves]
moves = [[int(m[1]),int(m[3]),int(m[5])] for m in moves]
stacks = [deque() for i in range(cols)]
for l in cargo:
    temp = []
    for i in range(cols):
        temp.append(l[i*4+1].strip())
    for i, q in enumerate(stacks):
        if temp[i]: q.append(temp[i])
stacks1=[deque(q) for q in stacks]
for m in moves:
    for i in range(m[0]):
        stacks1[m[2]-1].appendleft(stacks1[m[1]-1].popleft())
out = ''.join([s.popleft() for s in stacks1])
print('1. After the rearrangement procedure completes, what crate ends up on top of each stack? =>', out)
# End part I
# Your puzzle answer was HBTMTBSDC.

# Part II solution
for m in moves:
    temp=deque()
    for i in range(m[0]):
        temp.appendleft(stacks[m[1]-1].popleft())
    for i in range(m[0]):
        stacks[m[2]-1].appendleft(temp.popleft())
out = ''.join([s.popleft() for s in stacks])
print('2. After the rearrangement procedure completes, what crate ends up on top of each stack? =>', out)
# End part II
# Your puzzle answer was PQTJRSHWS.
