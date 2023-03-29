# BOJ 14613 너의 티어는
import sys
from math import comb
input = sys.stdin.readline

global W, L, D
W, L, D = map(float, input().split())
tier = [0, 0, 0, 0, 0]

def find_tier(w, l):
    score = 50*w - 50*l
    if score >= -1000 and score <= -501:
        return 0
    elif score >= -500 and score <= -1:
        return 1
    elif score >=0 and score <= 499:
        return 2
    elif score >=500 and score <= 999:
        return 3
    elif score >=1000 and score <= 1499:
        return 4

for w in range(21):
    for l in range(21-w):
        d = 20 - w - l
        p = W**w * L**l * D**d * comb(20, w) * comb(20-w, l)
        tier[find_tier(w, l)] += p

for t in tier:
    print(f'{t:.8f}')
