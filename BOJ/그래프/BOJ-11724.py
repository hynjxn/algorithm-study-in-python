# BOJ 11724 연결요소의 개수
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
def dfs(i):
    stack = []
    visited[i] = 1
    for e in graph[i]:
        if not visited[e]:
            stack.append(e)
    while stack:
        num = stack.pop(0)
        dfs(num)
    return 1

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        cnt += dfs(i)
print(cnt)