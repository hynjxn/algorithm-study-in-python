# BOJ 13549 숨바꼭질
import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())

q = deque([N]) # 시간 효율 위해 덱 사용
visited = [0] * 100001 # 방문 여부와 해당 지점 방문 시의 시간을 함께 기록

find = False
while q:
    X = q.popleft()
    if X == K:
        break
    temp = X
    while temp < K and temp != 0:
        temp = 2 * temp
        visited[temp] = visited[X]
        q.append(temp)
        if temp == K:
            find = True
            break
    if find == True:
        X = temp
        break

    sec = visited[X] + 1
    for next in [X-1, X+1]:
        if 0 <= next <= 100000 and visited[next] == 0:
            visited[next] = sec
            q.append(next)


print(visited[X])