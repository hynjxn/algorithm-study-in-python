# BOJ 7569 토마토 (BFS)
import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = []
q = deque()
# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for _ in range(H):
    temp = []
    for _ in range(N):
        temp.append(list(map(int, input().split())))
    tomato.append(temp)

# 모두 다 익은 토마토인 경우 출력하고 끝냄
allRipe = True
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                allRipe = False
                break
        if allRipe == False: break
    if allRipe == False: break

if allRipe == True:
    print(0)
    exit()

# 익은 토마토 위치 덱에 저장
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                q.append((i, j, k))
# BFS
while q:
    (i, j, k) = q.popleft()
    for d in range(6):
        a = i + dz[d]
        b = j + dy[d]
        c = k + dx[d]
        if a < 0 or a >= H or b < 0 or b >= N or c < 0 or c >= M\
            or tomato[a][b][c] != 0: continue
        if tomato[a][b][c] == 0:
            # 익은 토마토는 익는데 걸리는 날짜로 표시. 나중에 1 빼줘야 함
            tomato[a][b][c] = tomato[i][j][k] + 1
            q.append((a, b, c))

# 안 익은 토마토 있는지 확인 & 토마토 모두 익는데 걸리는 시간 확인
maxDay = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                print(-1)
                exit()
            if tomato[i][j][k] > maxDay:
                maxDay = tomato[i][j][k]

print(maxDay-1)
