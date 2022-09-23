# BOJ 1516 게임개발
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
time = ['_']
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for i in range(1, N+1):
    temp = list(map(int, input().split()))[:-1]
    time.append(temp[0])
    for j in temp[1:]:
        graph[j].append(i)
        indegree[i] += 1

q = deque()
result_time = [0] * (N+1)
for i in range(1, N+1):
    if indegree[i] == 0: # 진입 차수가 0인 노드를 덱에 추가
        q.append(i)
print(indegree)
while q:
    building = q.popleft()
    result_time[building] += time[building]
    for i in graph[building]:
        indegree[i] -= 1
        result_time[i] = max(result_time[i], result_time[building])
        if indegree[i] == 0:
            q.append(i)
print(graph)
for i in result_time[1:]:
    print(i)
