# https://adventofcode.com/2021/day/10

mk = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
cmk = { ')': 1, ']': 2, '}': 3, '>': 4 }
db, sg = ['()', '[]', '{}', '<>'], '([{<'

def sremove(l, d=True):
    tmp = db if d else sg
    for i in tmp: l=l.replace(i, '')
    return l
def cchar(c):
    return { '(': ')', '[': ']', '{': '}', '<': '>' }[c]

# file = open('./2021/day10/sample.txt', 'r')
file = open('./2021/day10/input.txt', 'r')
input = file.read().splitlines()

# Part I solution
scores=[]
err_score, compl_score = 0, 0
for l in input:
    check=0
    while check!=-4:
        check = l.find('()')+l.find('[]')+l.find('{}')+l.find('<>')
        l=sremove(l)
        
    if not set(l).issubset(set(sg)): # corrupted lines
        l=sremove(l, False)
        err_score+=mk[l[0]]
# print('What do you get if you add up all of the output values? => ', err_score)
# End part I

# Your puzzle answer was 343863.

# Part II solution
    else: # incomplete lines
        missing = [cchar(c) for c in l][::-1]
        for m in missing:
            compl_score*=5
            compl_score+=cmk[m]
        scores.append(compl_score)
        compl_score=0
scores=sorted(scores)

print('What is the middle score? => ', scores[len(scores)//2])
# End part II

# Your puzzle answer was 2924734236.
