import sys
from itertools import combinations
from collections import deque
import copy
input = sys.stdin.readline

N = int(input())
corr = []
teacher = []
blank = []
for i in range(N):
    corr.append(list(input().split()))
    for j in range(N):
        if corr[i][j] == 'T':
            teacher.append((i, j))
        elif corr[i][j] == 'X':
            blank.append((i, j))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs():
    for t in teacher:
        for i in range(4):
            nx, ny = t
            nx += dx[i]
            ny += dy[i]
            while 0<=nx<N and 0<=ny<N:
                if temp_corr[nx][ny] == 'S':
                    return False
                if temp_corr[nx][ny] == 'T' or temp_corr[nx][ny] == 'O':
                    break
                nx += dx[i]
                ny += dy[i]
    return True

for c in combinations(blank, 3):
    temp_corr = copy.deepcopy(corr)
    for x, y in c:
        temp_corr[x][y] = 'O'
    if bfs():
        print("YES")
        exit()
print("NO")