# BOJ 1149 RGB거리
import sys
input= sys.stdin.readline

N = int(input())
RGB_cost = [[0,0,0]]
for _ in range(N):
    RGB_cost.append(list(map(int, input().split())))
dp = [[0,0,0] for _ in range(N+1)]
for i in range(1, N+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2])+RGB_cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2])+RGB_cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1])+RGB_cost[i][2]
print(min(dp[N]))