import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    start, end, people = map(int, input().split())
    arr.append((start, end, people))


dp = [0] * 100001

for i in range(N):
        dp[i] = max(dp[i-1], dp[i-2]+arr[i][2], dp[i-3]+arr[i][2])

print(dp[N-1])