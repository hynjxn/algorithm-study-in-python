# BOJ 18427 함께 블록 쌓기
import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
# dp[i][j]: i번째 사람까지 계산해서 높이 j가 될 수 있는 경우의 수
# 높이 0이 될 수 있는 경우의 수 1을 미리 초기화
dp = [[1]+[0]*H for _ in range(N+1)]
for i in range(1, N+1):
    # i-1번 사람까지 계산한 dp 배열 가져오기
    dp[i] = dp[i-1][:]
    blocks = list(map(int, input().split()))
    for b in blocks:
        for j in range(b, H+1):
            # 현재 블록을 쌓았을 때 높이가 j가 되려면,
            # 이전 블록을 쌓았을 때까지 높이가 j-b임
            dp[i][j] += dp[i-1][j-b]
print(dp[N][H]%10007)
