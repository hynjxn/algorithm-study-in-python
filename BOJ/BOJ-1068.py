# BOJ 1068 트리
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
parent = list(map(int, input().split()))
X = int(input())

q = deque()
parent[X] = '_'
q.append(X)

while q:
    node = q.popleft()
    for i in range(N):
        if node == parent[i]:
            q.append(i)
            parent[i] = '_'

cnt = 0
for i in range(N):
    if parent[i] != '_' and i not in parent:
        cnt += 1

print(cnt)