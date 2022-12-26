# https://adventofcode.com/2022/day/9
abs1 = [1, -1]


def aligned(head, tail):
    return head[0] == tail[0] or head[1] == tail[1]


def same_col_touch(head, tail):
    return head[0] == tail[0] and head[1]-tail[1] in abs1


def same_line_touch(head, tail):
    return head[1] == tail[1] and head[0]-tail[0] in abs1


def diag_touch(head, tail):
    return (head[0]-tail[0])**2+(head[1]-tail[1])**2 == 2


def same_pos(head, tail):
    return head == tail


def touch(head, tail):
    return same_pos(head, tail) or same_col_touch(head, tail) or same_line_touch(head, tail) or diag_touch(head, tail)


def move_head(d):
    head = knots[-1]
    if d == 'R':
        head = head[0]+1, head[1]
    elif d == 'L':
        head = head[0]-1, head[1]
    elif d == 'U':
        head = head[0], head[1]+1
    else:
        head = head[0], head[1]-1  # move down
    return head


def get_dir(head, tail):
    if head[0] == tail[0]:  # aligned horizontally
        return 'U' if head[1] > tail[1] else 'D'
    # else they are aligned vertically
    return 'R' if head[0] > tail[0] else 'L'


def follow_moves(head, tail):
    if aligned(head, tail):  # move vertically or horizontally towards head
        direction = get_dir(head, tail)
        # print("aligned", head, tail)
        if direction == 'R':
            return tail[0]+1, tail[1]
        elif direction == 'L':
            return tail[0]-1, tail[1]
        elif direction == 'U':
            return tail[0], tail[1]+1
        else:
            return tail[0], tail[1]-1
    # move diagonaly towards head
    temp = head[0]-tail[0], head[1]-tail[1]
    temp = temp[0]//abs(temp[0]), temp[1]//abs(temp[1])
    return tail[0]+temp[0], tail[1]+temp[1]


file = open('input.txt', 'r')
# file = open('sample.txt', 'r')
# file = open('sample2.txt', 'r')
input = [l.split() for l in file.read().splitlines()]
input = [{"dir": l[0], "steps": int(l[1])} for l in input]

sz = 2  # or 10 for part 2
knots = [(0, 0)]*sz
tail, head = knots[0], knots[-1]
tail_positions = set([knots[0]])

for l in input:
    for i in range(l["steps"]):
        knots[-1] = move_head(l["dir"])
        for j in range(sz-2, -1, -1):
            if not touch(knots[j+1], knots[j]):
                temp = knots[j]
                knots[j] = follow_moves(knots[j+1], knots[j])
        tail_positions.add(knots[0])
out = len(tail_positions)
print('How many positions does the tail of the rope visit at least once? =>', out)
# End part I
# Your puzzle answer was 6256.

# Part II solution
# End part II
# Your puzzle answer was 2665.
