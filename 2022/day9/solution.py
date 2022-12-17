# https://adventofcode.com/2022/day/9
abs1 = [1, -1]
def aligned():
    return head[0]==tail[0] or head[1]==tail[1]
def same_col_touch():
    return head[0]==tail[0] and head[1]-tail[1] in abs1
def same_line_touch():
    return head[1]==tail[1] and head[0]-tail[0] in abs1
def diag_touch():
    return (head[0]-tail[0])**2+(head[1]-tail[1])**2 ==2
def same_pos():
    return head==tail
def touch():

    if same_pos():
        # print("# same_pos", head, tail)
        return True
    elif same_col_touch():
        # print("# same_col_touch", head, tail)
        return True
    elif same_line_touch():
        # print("# same_line_touch", head, tail)
        return True
    elif diag_touch():
        # print("# diag_touch", head, tail)
        return True
def next_head(d):
    # print("moving head", d)
    if d=='R': return head[0]+1, head[1]
    elif d=='L': return head[0]-1, head[1]
    elif d=='U': return head[0], head[1]+1
    return head[0], head[1]-1 # move down
def next_tail(d):
    # print("moving tail", d)
    if aligned(): # move in same direction
        if d=='R': return tail[0]+1, tail[1]
        elif d=='L': return tail[0]-1, tail[1]
        elif d=='U': return tail[0], tail[1]+1
        else: return tail[0], tail[1]-1
    else:
        temp = head[0]-tail[0], head[1]-tail[1]
        temp = temp[0]//abs(temp[0]), temp[1]//abs(temp[1])
        return tail[0]+temp[0], tail[1]+temp[1] # move diagonaly in the same direction
   

# file = open('input.txt', 'r')
file = open('sample.txt', 'r')
input = [l.split() for l in file.read().splitlines()]
tail, head = (0, 0), (0, 0)
tail_positions = set([tail])

for l in input:
    for i in range(int(l[1])):
        head = next_head(l[0])
        if not touch():
            tail = next_tail(l[0])
        # else:
            # print("touch at", head, tail)
        tail_positions.add(tail)
        # print(head, tail)
    # print()
out = len(tail_positions)
print('1. How many positions does the tail of the rope visit at least once? =>', out)
# End part I
# Your puzzle answer was 1453349.

# Part II solution
out = 0
# print('2. =>', out)
# End part II
# Your puzzle answer was 2948823.
