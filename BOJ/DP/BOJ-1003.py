# BOJ 1003 피보나치 함수
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    dp = [[1, 0], [0, 1]]+[[0, 0] for _ in range(N-1)]
    for i in range(2, N+1):
        for j in range(2):
            dp[i][j] = dp[i-1][j]+dp[i-2][j]
    print(*dp[N])