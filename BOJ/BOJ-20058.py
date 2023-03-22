#BOJ 20058 마법사 상어와 파이어스톰
import copy
import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())
ice_arr = []
for _ in range(2**N):
    ice_arr.append(list(map(int, input().split())))

L = list(map(int, input().split()))

dx=[1, 0, -1, 0]
dy=[0, 1, 0, -1]

# 배열 회전
def turn(arr, l):
    new_arr = [[0 for _ in range(2**N)] for _ in range(2**N)]
    # i, j : 부분 격자 기준점
    # a, b: 부분 격자 내에서 좌표 이동
    for i in range(0, 2**N, 2**l):
        for j in range(0, 2**N, 2**l):
            for a in range(2**l):
                for b in range(2**l):
                    new_arr[i+a][j+b] = arr[i+2**l-1-b][j+a]
    return new_arr

# 얼음 3개 미만 인접 칸 처리
def reduce_ice(arr):
    new_arr = copy.deepcopy(arr)
    for x in range(2**N):
        for y in range(2**N):
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<2**N and 0<=ny<2**N:
                    if arr[nx][ny] > 0:
                        cnt +=1
            if cnt < 3:
                new_arr[x][y] -= 1
    return new_arr


for i in range(Q):
    ice_arr = turn(ice_arr, L[i])
    ice_arr = reduce_ice(ice_arr)

ice_sum = 0
max_ice = 0
visited = [[0 for _ in range(2**N)] for _ in range(2**N)]
for i in range(2**N):
    for j in range(2**N):
        if ice_arr[i][j]>0:
            ice_sum += ice_arr[i][j]
        if not visited[i][j] and ice_arr[i][j]>=1:
            q = deque([[i,j]])
            visited[i][j] = 1
            ice_size = 1
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<2**N and 0<=ny<2**N and not visited[nx][ny] and ice_arr[nx][ny]>=1:
                        ice_size += 1
                        q.append([nx,ny])
                        visited[nx][ny]=1
            max_ice = max(max_ice, ice_size)

print(ice_sum)
print(max_ice)



