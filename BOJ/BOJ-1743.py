# BOJ 1743 음식물 피하기 (DFS)
import sys
sys.setrecursionlimit(100000) # 안 쓰면 Recursion Error 뜸
input = sys.stdin.readline

N, M, K = map(int, input().split())
tongro = [[0] * M for _ in range(N)]

for _ in range(K):
    x, y = map(int, input().split())
    tongro[x-1][y-1] = 1 # 배열의 [0][0]이 (1,1)와 같기 때문

cnt = 0 # dfs로 이어져 있는 칸을 세기 위한 변수
max = 0 # 가장 큰 음식물 크기 담는 변수

def dfs(i, j):
    global cnt
    if i < 0 or i >= N or \
            j < 0 or j >= M or \
            tongro[i][j] != 1:
                return

    cnt += 1
    tongro[i][j] = '_' # 이미 탐색한 음식물 visited 처리

    # 상하좌우 탐색
    dfs(i+1, j)
    dfs(i, j+1)
    dfs(i-1, j)
    dfs(i, j-1)


for i in range(N):
    for j in range(M):
        if tongro[i][j] == 1:
            dfs(i, j)
            temp = cnt
            cnt = 0
            if max < temp:
                max = temp
print(max)