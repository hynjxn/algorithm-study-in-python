#BOJ 22865 가장 먼 곳
import sys
import heapq
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
A, B, C = map(int, input().split())
M = int(input())
for _ in range(M):
    D, E, L = map(int, input().split())
    graph[D].append([E, L])
    graph[E].append([D, L])

def dijkstra(graph, start):
    dist = [987654321 for _ in range(N+1)]
    dist[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    while q:
        cur_dist, cur_dest = heapq.heappop(q)
        if dist[cur_dest] < cur_dist:
            continue
        for new_dest, new_dist in graph[cur_dest]:
            if cur_dist + new_dist < dist[new_dest]:
                dist[new_dest] = cur_dist+new_dist
                heapq.heappush(q, [dist[new_dest], new_dest])
    return dist

dist_A = dijkstra(graph, A)
dist_B = dijkstra(graph, B)
dist_C = dijkstra(graph, C)
temp_dist = 0
furthest = 0
for i in range(1, N+1):
    if temp_dist < min(dist_A[i], dist_B[i], dist_C[i]):
        temp_dist = min(dist_A[i], dist_B[i], dist_C[i])
        furthest = i

print(furthest)