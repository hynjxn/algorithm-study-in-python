# BOJ 2839 설탕배달
import sys
input = sys.stdin.readline

# 그리디 풀이
# N = int(input())
# answer = -1
# if N%5==0:
#     answer = N//5
# else:
#     x = N // 5
#     while x>=0:
#         if (N - 5*x) % 3 == 0:
#             y = (N - 5*x) // 3
#             answer = x+y
#             break
#         else:
#             x -= 1
# print(answer)

# DP 풀이
N = int(input())
dp = [-1 for _ in range(5001)]
dp[3] = 1
dp[5] = 1
for i in range(6, N+1):
    if dp[i-3] == -1 and dp[i-5] != -1:
        dp[i] = dp[i-5]+1
    elif dp[i-5] == -1 and dp[i-3] != -1:
        dp[i] = dp[i-3]+1
    elif dp[i-5] != -1 and dp[i-3] !=-1:
        dp[i] = min(dp[i-3]+1, dp[i-5]+1)

print(dp[N])