# BOJ 17281 (야구?)
import sys
import itertools
input = sys.stdin.readline

orders=[]
for e in itertools.permutations([2,3,4,5,6,7,8,9], 8):
    e = list(e)
    e.insert(3, 1)
    orders.append(e)

N = int(input())
inning = []
for _ in range(N):
    inning.append(list(map(int, input().split())))

max_score = 0
for order in orders:
    x = 0
    score = 0
    for i in range(N):
        out = 0
        field = [0, 0, 0]
        while out != 3:
            next_taja = order[x % 9] -1
            if inning[i][next_taja] == 0:
                out += 1
            elif inning[i][next_taja] == 1:
                score += field[2]
                field[2] = 1 if field[1] else 0
                field[1] = 1 if field[0] else 0
                field[0] = 1
                print(score, inning[i], field)
            elif inning[i][next_taja] == 2:
                score += (field[2] + field[1])
                field[2] = 1 if field[0] else 0
                field[1], field[0] = 1, 0
            elif inning[i][next_taja] == 3:
                score += (field[2] + field[1] + field[0])
                field[2], field[1], field[0] = 1, 0, 0
            elif inning[i][next_taja] == 4:
                score += field[2] + field[1] + field[0] + 1
                field = [0, 0, 0]
            x += 1
    if score > max_score:
        max_score = score

print(max_score)


