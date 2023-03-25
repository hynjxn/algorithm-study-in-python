# BOJ 11725 트리의 부모 찾기
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

tree = [[] for i in range(N+1)]
parent = [0] * (N+1)

for i in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

q = deque([1])
while q: # bfs로 부모 탐색
    p_node = q.popleft()
    for n_node in tree[p_node]:
        if parent[n_node] == 0:
            parent[n_node] = p_node
            q.append(n_node)

for i in parent[2:]:
    print(i)