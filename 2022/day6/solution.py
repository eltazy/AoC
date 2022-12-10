# https://adventofcode.com/2022/day/6

def get_marker_pos(str, n):
    for i in range(n-1, len(str)):
        sub = stream[i-n+1:i+1]
        if len(set(sub)) == n:
            return i+1


file = open('input.txt', 'r')
# file = open('sample.txt', 'r')
stream = file.read().splitlines()[0]

# Part I solution
out = get_marker_pos(stream, 4)
print('1. How many characters need to be processed before the first start-of-packet marker is detected? =>', out)
# # End part I
# # Your puzzle answer was 1093.

# # Part II solution
out = get_marker_pos(stream, 14)
print('2. How many characters need to be processed before the first start-of-message marker is detected? =>', out)
# End part II
# Your puzzle answer was 3534.
