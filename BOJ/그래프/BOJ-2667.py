# BOJ 2667 단지번호붙이기
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr=[list(map(int, input().rstrip())) for _ in range(N)]

danji = []
visited = [[0] * N for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def BFS(i, j):
    cnt = 1
    q = deque([[i, j]])
    arr[i][j] = 0

    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and arr[nx][ny]==1:
                    arr[nx][ny] = 0
                    q.append([nx, ny])
                    cnt += 1
    danji.append(cnt)

for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j] == 1:
            BFS(i, j)
danji.sort()
print(len(danji))
print(*danji, sep='\n')