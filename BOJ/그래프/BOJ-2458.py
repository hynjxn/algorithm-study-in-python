# BOJ 2458 키 순서
# 프로그래머스 '순위' 문제와 동일
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
compares = [list(map(int, input().split())) for _ in range(M)]
ans = 0
INF = int(1e9)
graph = [[INF] * N for _ in range(N)]
for i in range(N):
    graph[i][i] = 0
for w, l in compares:
    graph[w - 1][l - 1] = 1
    graph[l - 1][w - 1] = -1

for i in range(N):
    for j in range(N):
        if graph[i][j] != INF:
            continue
        for k in range(N):
            if graph[i][k] == graph[k][j] and graph[i][k]!=INF:
                graph[i][j] = graph[i][k]
                graph[j][i] = -graph[i][k]
                break

for i in range(N):
    if INF not in graph[i]:
        ans += 1
print(ans)