# BOJ 17070 파이프 옮기기 1
# DP로 해결
import sys
input = sys.stdin.readline
arr = []
N = int(input())
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[[0] * N for _ in range(N)] for _ in range(3)]
# 0: 가로 1: 세로 2: 대각선
dp[0][0][1] = 1 # 처음 시작을 가로로 시작

# 맨 첫 줄 채우기 (가로 방향만 가능)
for i in range(2, N):
    if arr[0][i] != 0:
        break
    dp[0][0][i] = 1

for i in range(1, N):
    for j in range(2, N):
        # 대각선
        if arr[i][j] == 0 and arr[i-1][j] == 0 and arr[i][j-1] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
        if arr[i][j] == 0:
            # 가로
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            # 세로
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]

answer = sum(dp[i][N-1][N-1] for i in range(3))
print(answer)