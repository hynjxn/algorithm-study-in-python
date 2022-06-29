# BOJ 1303 전쟁 - 전투 (DFS)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 가로 M: 세로
battle_gnd = []
w_power, b_power = 0, 0
cnt = 0
for _ in range(M):
    battle_gnd.append(list(map(str, input())))

def dfs_w(i, j): # 흰색 병사 탐색
    # 이어진 흰색 병사 없을 경우 or 벽면에 다다른 경우 종료
    if i < 0 or i >= M or \
            j < 0 or j >= N or \
            battle_gnd[i][j] != 'W':
                return
    global cnt
    cnt += 1
    # 이미 탐색한 병사 처리
    battle_gnd[i][j] = '_'

    # 상하좌우 탐색
    dfs_w(i+1, j)
    dfs_w(i, j+1)
    dfs_w(i-1, j)
    dfs_w(i, j-1)

def dfs_b(i, j): # 청색 병사 탐색
    # 이어진 청색 병사 없을 경우 or 벽면에 다다른 경우 종료
    if i < 0 or i >= M or \
            j < 0 or j >= N or \
            battle_gnd[i][j] != 'B':
                return
    global cnt
    cnt += 1
    # 이미 탐색한 병사 처리
    battle_gnd[i][j] = '*'

    # 상하좌우 탐색
    dfs_b(i+1, j)
    dfs_b(i, j+1)
    dfs_b(i-1, j)
    dfs_b(i, j-1)

# dfs 실행
for i in range(M):
    for j in range(N):
        if battle_gnd[i][j] == 'W':
            dfs_w(i, j)
            w_power += cnt*cnt
            cnt = 0
        elif battle_gnd[i][j] == 'B':
            dfs_b(i, j)
            b_power += cnt*cnt
            cnt = 0

print(w_power, b_power)
