# BOJ 1520 내리막길
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

M, N = map(int, input().split())
arr = []
for _ in range(M):
    arr.append(list(map(int, input().split())))
dp = [[-1] * N for _ in range(M)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    print(x, y)
    if x == M-1 and y == N-1:
        return 1
    if dp[x][y]!=-1:
        return dp[x][y]
    temp = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<M and 0<=ny<N and arr[x][y] > arr[nx][ny]:
            temp += dfs(nx, ny)
    dp[x][y]=temp
    return dp[x][y]
print(dfs(0,0))
