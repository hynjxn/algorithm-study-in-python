# BOJ 12865 평범한 배낭
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
things = [(0,0)]+[tuple(map(int, input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    dp[i] = dp[i-1][:]
    w, v = things[i]
    for j in range(w, K+1):
        dp[i][j] = max(dp[i-1][j-w]+v, dp[i-1][j])
print(dp[N][K])