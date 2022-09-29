# BOJ 15486 퇴사 2
# DP
import sys
input = sys.stdin.readline

N = int(input())
T = [0] * (N+1)
P = [0] * (N+1)
for i in range(1, N+1):
    t, p = map(int, input().split())
    T[i], P[i] = t, p

dp = [0] * (N+2)
# 끝나는 날부터 역으로 채움
for i in range(N, 0, -1):
    # 현재 날 + 기간이 퇴사 일을 넘어가는 경우 해당 일 할수 없음
    if i + T[i] > N + 1:
        dp[i] = dp[i+1]
        continue
    # 현재 일을 할 경우 -> 끝나는 날의 dp 값에 현재 이익을 더한 값
    # 이를 현재 일을 하지 않을 경우의 값과 비교
    dp[i] = max(dp[i+1], P[i]+dp[i+T[i]])

print(dp[1])