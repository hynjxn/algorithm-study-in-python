# BOJ 1697 숨바꼭질 (BFS)
import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())

q = deque([N]) # 시간 효율 위해 덱 사용
visited = [0] * 100001 # 방문 여부와 해당 지점 방문 시의 시간을 함께 기록

while q:
    X = q.popleft()
    if X < 0 and X > 100000:
        continue
    if X == K:
        break

    sec = visited[X] + 1
    for next in [X-1, X+1, X*2]:
        if 0 <= next <= 100000 and visited[next] == 0:
            visited[next] = sec
            q.append(next)


print(visited[X])