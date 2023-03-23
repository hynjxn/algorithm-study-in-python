# BOJ 2252 줄 세우기
# 위상 정렬 : 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열
# 큐(덱)를 사용해 진입차수가 0인 모든 노드를 큐에 삽입
# 큐에서 원소를 꺼내면 해당 노드에서 나가는 간선을 제거 -> 새롭게 진입차수 0이 되는 노드 탐색
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
indegree = [0] * (N+1) # 진입 차수
graph = [[] for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1 # 진입 차수를 1 증가시킴

result = []
q = deque()

for i in range(1, N+1):
    if indegree[i] == 0: # 진입 차수가 0인 노드를 덱에 추가
        q.append(i)

while q:
    student = q.popleft()
    result.append(student)
    for i in graph[student]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

for i in result:
    print(i, end=' ')