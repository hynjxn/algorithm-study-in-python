import sys
input = sys.stdin.readline


N = int(input())
balloon = list(range(1, N+1))
ball_paper = list(map(int, input().split()))
answer = []

idx = 0
num = ball_paper.pop(idx)
answer.append(balloon.pop(idx))

while ball_paper:
    if num > 0:
        idx = (idx + num -1) % len(ball_paper)
    else:
        idx = (idx + num) % len(ball_paper)

    num = ball_paper.pop(idx)
    answer.append(balloon.pop(idx))

for _ in answer:
    print(_, end=' ')