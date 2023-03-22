# BOJ 10026 적록색약
import sys
input = sys.stdin.readline

N = int(input())
arr = []
visited = [[0]*N for _ in range(N)]
for _ in range(N):
    arr.append(list(input().rstrip()))

dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]

def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and arr[x][y] == arr[nx][ny]:
            dfs(nx, ny)
    return 1

ans = 0
ans_RG = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            ans += dfs(i, j)

visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            ans_RG += dfs(i, j)
print(ans, ans_RG)