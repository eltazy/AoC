# https://adventofcode.com/2022/day/4
def get_ranges(s):
    s = [int(i) for i in s.split('-')]
    return set(range(s[0], s[1]+1))


def total_overlap(u: set, v: set):
    t = u if len(u) > len(v) else v
    return u.union(v) == t


def some_overlap(u: set, v: set):
    return bool(u.intersection(v))


file = open('input.txt', 'r')
# file = open('sample.txt', 'r')
raw_input = file.read().splitlines()

# Part I solution
raw_input = [l.split(',') for l in raw_input]
raw_input = [[get_ranges(e) for e in pair] for pair in raw_input]
input1 = [total_overlap(pair[0], pair[1]) for pair in raw_input]
out = len([b for b in input1 if b])
print('1. In how many assignment pairs does one range fully contain the other? =>', out)
# End part I
# Your puzzle answer was 441.

# Part II solution
input2 = [some_overlap(pair[0], pair[1]) for pair in raw_input]
out = len([b for b in input2 if b])
print('2. In how many assignment pairs do the ranges overlap? =>', out)
# End part II
# Your puzzle answer was 861.
