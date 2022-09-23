# BOJ 11559
import sys
input = sys.stdin.readline
from collections import deque

field = []
for _ in range(12):
    temp = list(input().split())
    field.append(temp)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
result = 0

def bfs(a, b, color):
    q = deque([(a, b)])
    visited = [[0]* 6 for _ in range(12)]
    visited[a][b] = 1
    cnt = 0
    puyo = False
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx > 11 or ny < 0 or ny > 5:
                continue
            if field[nx][ny] == color and visited[nx][ny] == 0:
                q.append(nx, ny)
                visited[nx][ny] = 1
                cnt += 1

    if cnt >=4:
        puyo = True
    return puyo

while 1:
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.':
                if bfs(i, j, field[i][j]):
                    result += 1