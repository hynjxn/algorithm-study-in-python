# BOJ 14852 타일 채우기 3
# DP
import sys
input = sys.stdin.readline
N = int(input())

dp = [[1, 1], [2 ,3], [7, 10]]+[[0, 0] for _ in range(N)]
# dp[i][0] : 2*i 크기 타일을 채울 수 있는 경우의 수
# dp[i][1] : dp[1][0]부터 dp[i][0]까지의 합

for i in range(3, N+1):
    dp[i][0] = (dp[i-1][1]*2 +dp[i-2][0])%1000000007
    dp[i][1] = (dp[i-1][1]+dp[i][0])%1000000007

print(dp[N][0])