# https://adventofcode.com/2021/day/8

# Equation (1)
def getA(s7, o1):
    return (set(s7)-set(o1)).pop()
# Equation (2)
def getG(a, e, f4, e8):
    tmp = set(e8)-set(f4)-set([a, e])
    return tmp.pop()
# Equation (2)
def getE(f4, s6):
    t1, t2, t3 = set(s6[0])-set(f4), set(s6[1])-set(f4), set(s6[2])-set(f4)
    u = set(s6[0]).union(s6[1]).union(s6[2])
    i = set(s6[0]).intersection(s6[1]).intersection(s6[2])
    return (u-i-set(f4)).pop()
# Equation (3)
def getC(f5, s6, arr):
    res = []
    tmp = f5+s6
    for t in tmp:
        res.append(set(t)-set(arr))
    res = sorted([t.pop() for t in res if len(t)==1])
    return res[0] if res.count(res[0])==1 else res[2]
# Equation (4)
def getF(c, o1):
    tmp = set(o1)
    tmp.remove(c)
    return tmp.pop()
# Equation (5)
def getB(e8, arr):
    tmp = set(e8)
    for c in arr: tmp.remove(c)
    return tmp.pop()
# Equation (5)
def getBD(o1, s6, arr):
    tmp = set(o1).union(arr)
    t=[]
    for s in s6:
        t.append(set(s)-tmp)
    t = sorted(t, key=len)
    b = t[0].pop()
    d = t[1]
    d.remove(b)
    d=d.pop()
    return b, d
def read7(s):
    return ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg'].index(''.join(sorted(s)))
def decode7(s, arr):
    res=''
    for c in s:
        res+=str(list(arr.keys())[list(arr.values()).index(c)])
    return res


# file = open('./2021/day8/sample.txt', 'r')
file = open('./2021/day8/input.txt', 'r')
input = file.read().splitlines()
signals = [str.split('|')[0].split() for str in input]
outputs = [str.split('|')[1].split() for str in input]
count = 0

# Part I solution
# fsizes = [2, 3, 4, 7]
# for out in outputs:
#     for o in out:
#         if len(o) in fsizes: count+=1
# End part I

# Your puzzle answer was 352.

# Part II solution

segments = ['']*7
for i, sg in enumerate(signals):
    one, four, = [s for s in sg if len(s)==2][0], [s for s in sg if len(s)==4][0]
    seven, eight = [s for s in sg if len(s)==3][0], [s for s in sg if len(s)==7][0]
    fivers, sixers = [s for s in sg if len(s)==5], [s for s in sg if len(s)==6]
    a,b,c,d,e,f,g = '','','','','','',''
    a = getA(seven, one)
    e = getE(four, sixers)
    g = getG(a, e, four, eight)
    b, d = getBD(one, sixers, [a, e, g])
    c = getC(fivers, sixers, [a, b, d, e, g])
    f = getF(c, one)
    res=''
    for out in outputs[i]:
        t = decode7(out, { 'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f, 'g':g })
        t=read7(t)
        res+=str(t)
    count+=int(res)
# End part II

print('What do you get if you add up all of the output values? => ', count)

# Your puzzle answer was 936117.
