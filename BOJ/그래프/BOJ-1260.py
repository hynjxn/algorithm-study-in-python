# BOJ 1260 DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
# graph_1 = [[0] * (N + 1) for _ in range(N + 1)]

visited_d = [0] * (N+1)
visited_b = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

def dfs(start_node):
    print(start_node, end=' ')
    visited_d[start_node] = 1
    for i in graph[start_node]:
        if visited_d[i] == 0:
            dfs(i)

def bfs(start_node):
    q = deque()
    q.append(start_node)
    visited_b[start_node] = 1
    while q:
        node = q.popleft()
        print(node, end=' ')
        for i in graph[node]:
            if visited_b[i] == 0:
                q.append(i)
                visited_b[i] = 1
dfs(V)
print()
bfs(V)