# BOJ 1405 미친 로봇
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
N, e, w, s, n = map(int, input().split())
graph = [[0]*(2*N+1) for _ in range(2*N+1)]
p= [e/100, w/100, s/100, n/100]

ans = 0
def dfs (x, y, cnt, percent):
    global ans
    if cnt == N:
        ans += percent
        return
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if graph[nx][ny] != 0:
            continue
        dfs(nx,ny,cnt+1, percent*p[i])
        graph[nx][ny] = 0 # 이전의 탐색에서 거쳐갔을 수도 있는 부분 해제

dfs(N, N, 0, 1)
print(ans)
