# BOJ 1916 최소비용 구하기

import sys
input = sys.stdin.readline
import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [1000000000 for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
start, end = map(int, input().split())
distance[start] = 0
q = []
heapq.heappush(q, [0, start])
while q:
    cur_dist, cur_node = heapq.heappop(q)
    if distance[cur_node] < cur_dist:
        continue
    for e, c in graph[cur_node]:
        if distance[e] > cur_dist + c:
            distance[e] = cur_dist + c
            heapq.heappush(q, [distance[e], e])

print(distance[end])