# https://adventofcode.com/2021/day/9

def islp(arr, x, y):
    return int(arr[x][y])<min(neighbours(arr, x, y))

def neighbours(arr, x, y):
    return [int(arr[p[0]][p[1]]) for p in neighboursXY(arr, x, y)]

def neighboursXY(m, x, y):
    sx, sy = len(m[0]), len(m)
    res=[]
    if x: res.append((x-1, y))
    if y: res.append((x, y-1))
    if x<sy-1: res.append((x+1, y))
    if y<sx-1: res.append((x, y+1))
    return res
def map_terrain(m, lps, counter):
    for p in lps:
        res=[p for p in neighboursXY(m, p[0], p[1]) if m[p[0]][p[1]]=='.']
        for n in res:
            m[n[0]][n[1]]=m[p[0]][p[1]]
            counter[int(m[p[0]][p[1]])]+=1
        lps.extend(res)
def all_mapped(m, pts):
    for p in pts:
        if m[p[0]][p[1]]=='.': return False
    return True



# file = open('./2021/day9/sample.txt', 'r')
file = open('./2021/day9/input.txt', 'r')
input = file.read().splitlines()
input = [[int(c) for c in l] for l in input]
# risk = 0
# for i, line in enumerate(input):
#     for j, p in enumerate(line):
#         if islp(input, i, j): risk+=input[i][j]+1
# Part I solution

# End part I

# Your puzzle answer was 508.

# Part II solution
amap = [['.' for s in l] for l in input]
lps = []
count=0
for i, line in enumerate(input):
    for j, p in enumerate(line):
        if islp(input, i, j):
            amap[i][j]=str(count)
            lps.append((i,j))
            count+=1
        if p==9: amap[i][j] = u"\u2592"

sol = { n:1 for n in range(len(lps)) }
mapped = lps
for i, line in enumerate(amap):
    for j, p in enumerate(line):
        if amap[i][j].isdigit(): map_terrain(amap, mapped, sol)
sol = [n for n in sorted(list(sol.values()))][-3:]

# print full map
print(''.join([u"\u2592"]*(len(input[0])+2)))
for l in amap: print('{}{}{}'.format(u"\u2592", ''.join([' ' if c.isdigit() else c for c in l]), u"\u2592"))
print(''.join([u"\u2592"]*(len(input[0])+2)))

# End part II

print('What do you get if you add up all of the output values? => ', sol[0]*sol[1]*sol[2])

# Your puzzle answer was 936117.
