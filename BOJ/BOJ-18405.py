#BOJ 18405 경쟁적 전염
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
virus = [] # 값, 시간, 좌표
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] != 0:
            virus.append([arr[i][j], 0, i, j])
S, X, Y = map(int, input().split())

dx=[1, 0, -1, 0]
dy=[0, 1, 0, -1]

virus.sort()
q = deque(virus)
while q:
    v, t, x, y = q.popleft()
    if t == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 0:
            arr[nx][ny] = v
            q.append([v, t+1, nx, ny])


print(arr[X-1][Y-1])
