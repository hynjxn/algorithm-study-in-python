# BOJ 1753 최단경로
import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

dist = [987654321 for _ in range(V+1)]
dist[start] = 0
q = []
heapq.heappush(q, [dist[start], start])

while q:
    cur_dist, cur_dest = heapq.heappop(q)
    if dist[cur_dest] < cur_dist:
        continue
    for new_dest, new_dist in graph[cur_dest]:
        distance = cur_dist + new_dist
        if distance < dist[new_dest]:
            dist[new_dest] = distance
            heapq.heappush(q, [distance, new_dest])


for i in range(1, V+1):
    if dist[i] == 987654321:
        print("INF")
    else:
        print(dist[i])