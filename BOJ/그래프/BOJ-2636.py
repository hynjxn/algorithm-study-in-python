# BOJ 2636 - 치즈
import sys
from collections import deque
input = sys.stdin.readline

dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]

a, b = map(int, input().split()) # a: 세로, b: 가로
cheese = []
for _ in range(a):
    cheese.append(list(map(int, input().split())))

# 공기(0)와 닿은 치즈(1)를 bfs로 탐색.
# 치즈 속의 구멍은 bfs과정에서 패스됨


def bfs():
    q = deque([[0, 0]]) # 공기를 담는 큐
    visited = [[0] * b for _ in range(a)]
    cnt = 0 # 사라지는 치즈 개수
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<a and 0<=ny<b and visited[nx][ny]==0:
                if cheese[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                else: # 공기와 닿은 치즈
                    cheese[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
    return cnt
time = 0
ans = []
while True:
    cnt = bfs()
    ans.append(cnt)
    if cnt == 0:
        break
    time += 1

print(time)
print(ans[-2])




