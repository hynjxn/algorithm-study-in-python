# BOJ 1912 연속합
import sys
input = sys.stdin.readline

n = int(input())
arr = [0]+list(map(int, input().split()))
dp = [-1000 for _ in range(n+1)]
dp[1] = arr[1]
for i in range(1, n+1):
    dp[i] = max(dp[i-1]+arr[i], arr[i])
print(max(dp))
