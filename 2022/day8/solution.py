# https://adventofcode.com/2022/day/8
def visibility(x, y):
    Nb, Nn = is_visible_N(x, y)
    Sb, Sn = is_visible_S(x, y)
    Wb, Wn = is_visible_W(x, y)
    Eb, En = is_visible_E(x, y)
    return (Eb or Wb or Sb or Nb), (En * Wn * Sn * Nn)


def is_visible_N(y, x):
    trees = 0
    for i in range(y-1, -1, -1):
        if grid[y][x] > grid[i][x]:
            trees += 1
        if grid[y][x] <= grid[i][x]:
            return False, trees+1
    return True, trees


def is_visible_S(y, x):
    trees = 0
    for i in range(y+1, nl):
        if grid[y][x] > grid[i][x]:
            trees += 1
        if grid[y][x] <= grid[i][x]:
            return False, trees+1
    return True, trees


def is_visible_W(y, x):
    trees = 0
    for i in range(x-1, -1, -1):
        if grid[y][x] > grid[y][i]:
            trees += 1
        if grid[y][x] <= grid[y][i]:
            return False, trees+1
    return True, trees


def is_visible_E(y, x):
    trees = 0
    for i in range(x+1, nc):
        if grid[y][x] > grid[y][i]:
            trees += 1
        if grid[y][x] <= grid[y][i]:
            return False, trees+1
    return True, trees


file = open('input.txt', 'r')
# file = open('sample.txt', 'r')
grid = file.read().splitlines()
grid = [[int(h) for h in list(l)] for l in grid]
nl, nc = len(grid), len(grid[0])

# Part I solution
visible_trees, scenic_views = 0, []
for i in range(1, nl-1):
    for j in range(1, nc-1):
        visible, scene = visibility(i, j)
        scenic_views.append(scene)
        if visible:
            visible_trees += 1
out = (nl+nc)*2-4 + visible_trees
print('1. How many trees are visible from outside the grid? =>', out)
# End part I
# Your puzzle answer was 1794.

# Part II solution
out = max(scenic_views)
print('2. What is the highest scenic score possible for any tree? =>', out)
# End part II
# Your puzzle answer was 199272.
