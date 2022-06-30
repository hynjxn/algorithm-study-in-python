# BOJ 2178 미로 탐색 (BFS)
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
miro = [] # 미로 담는 배열
dist = [] # 미로의 해당 위치까지 도달하는 데 지나는 칸 수
[dist.append([0]*M) for _ in range(N)]
[miro.append(list(map(str, input().rstrip()))) for _ in range(N)]
q = deque([(0, 0)])
dist[0][0] = 1

while q:
    temp = q.popleft()
    X, Y =temp[0], temp[1]
    if X == M-1 and Y == N-1: break

    for (i, j) in [(Y-1, X), (Y, X-1), (Y+1, X), (Y, X+1)]:
        if 0 <= j <= M - 1 and 0 <= i <= N - 1 \
            and miro[i][j] == '1' and dist[i][j] == 0:
                    q.append((j,i))
                    dist[i][j] = dist[Y][X] + 1

print(dist[N-1][M-1])