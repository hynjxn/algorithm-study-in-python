# BOJ 14501 퇴사
N = int(input())
TP = [[0, 0]]
for _ in range(N):
    TP.append(list(map(int, input().split())))
dp = [0] * (N+2)
for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1])
    if i+TP[i][0] > N+1:
        continue
    dp[i+TP[i][0]] = max(dp[i+TP[i][0]], dp[i]+TP[i][1])
print(max(dp))