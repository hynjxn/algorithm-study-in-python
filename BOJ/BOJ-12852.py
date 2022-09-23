# BOJ 12852 1로 만들기 2
import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
dp = [0] * 1000001
x = [0] * 1000001
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    x[i] = i-1
    if i % 3 == 0 and dp[i//3] +1 < dp[i]:
        dp[i] = dp[i//3] + 1
        x[i] = i//3
    if i % 2 == 0 and dp[i//2] +1 < dp[i]:
        dp[i] = dp[i//2] + 1
        x[i] = i//2

print(dp[N])
now = N
while now != 0:
    print(now, end=' ')
    now = x[now]