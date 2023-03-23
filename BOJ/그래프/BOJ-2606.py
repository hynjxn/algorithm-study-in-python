# BOJ 2606 바이러스
import sys
from collections import deque
input = sys.stdin.readline

com = int(input())
graph = [[0] * (com+1) for _ in range(com+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
cnt = 0
q = deque([1])
visited = [0] * (com+1)
visited[1] = 1
while q:
    x = q.popleft()
    for i in range(1, com+1):
        if graph[x][i]==1 and not visited[i]:
            q.append(i)
            visited[i] = 1
            cnt += 1

print(cnt)