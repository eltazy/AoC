# https://adventofcode.com/2022/day/2

def defeating_hand(h):
    return {"A": "Y", "B": "Z", "C": "X"}[h]

hand_default_scores = {"X": 1, "Y": 2, "Z": 3}
encrypted_hand =  {"A": "X", "B": "Y", "C": "Z"}

def opp_has_won(opp, you):
    return (opp, you) in [("X", "Z"),("Y", "X"),("Z", "Y")]

def play_score(opp, you):
    s = hand_default_scores[you]
    if opp_has_won(encrypted_hand[opp], you): return s  # win
    elif encrypted_hand[opp]==you:
        return s+3  # draw
    return s+6  # loss


file = open('input.txt', 'r')
# file = open('sample.txt', 'r')
input = [l.split(" ") for l in file.read().splitlines()]

# Part I solution
total = 0
for play in input:
    total += play_score(play[0], play[1])
print('What would your total score be if everything goes exactly according to your strategy guide? => ', total)
# End part I

# Your puzzle answer was 14069.

# Part II solution
def hand_for_outcome(h, out):
    if out=="Y": #draw
        return encrypted_hand[h]
    elif out=="X": # loss
        return {"A": "Z", "B": "X", "C": "Y"}[h]
    else: # you win
        return {"A": "Y", "B": "Z", "C": "X"}[h]

def play_score2(opp, out):
    you = hand_for_outcome(opp, out)
    s = hand_default_scores[you]
    if opp_has_won(encrypted_hand[opp], you): return s  # loss
    elif encrypted_hand[opp]==you:
        return s+3  # draw
    return s+6  # win

total = 0
for play in input:
    total += play_score2(play[0], play[1])

print('What would your total score be if everything goes exactly according to your strategy guide? => ', total)
# End part II

# Your puzzle answer was .
