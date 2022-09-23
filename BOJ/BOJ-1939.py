# BOJ 1939 중량제한
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [{} for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    if graph[A][B]:
        graph[A][B] = max(graph[A][B], C)
        graph[B][A] = graph[A][B]
    else:
        graph[A][B] = C
        graph[B][A] = C
i, j = map(int, input().split())

def bfs(c):
    q = deque([i])
    visited = [False for _ in range(N+1)]
    visited[i] = True
    while q:
        x = q.popleft()
        if x == j:
            return True # 도착 지점을 해당 무게로 방문 가능한 경우
        for node, limit in graph[x].items():
            if visited[node] == False and limit >= c:
                q.append(node)
                visited[node] = True
    return False # 도착 지점을 해당 무게로 방문 할 수 없는 경우

# 근데 이분탐색을 왜 써야하는지 이해하지 못했음
min, max = 1, 1000000000
result = min
while min <=max:
    mid = (min+max) // 2
    if bfs(mid):
        result = mid
        min = mid+1
    else:
        max = mid - 1

print(result)