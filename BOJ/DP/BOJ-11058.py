#BOJ 11058 크리보드
import sys
input = sys.stdin.readline

N = int(input())
dp = [i for i in range(N+1)]
buf = 0
for i in range(6, N+1):
    # ^A^C^V / ^A^C^V^V / ^A^C^V^V^V ---> 이 이상은 ^A^C^V^A^C^V가 무조건 최대이므로
    dp[i] = max(2*dp[i-3],3*dp[i-4], 4*dp[i-5] )
print(dp[N])