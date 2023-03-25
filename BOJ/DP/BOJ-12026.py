# BOJ 12026 BOJ 거리
# DP로 해결
import sys
input = sys.stdin.readline

N = int(input())
block = list(input().rstrip())
dp = [0]+[sys.maxsize for _ in range(N)]

start_link = {'B':'J', 'O':'B', 'J':'O'} # 앞에 와야 하는 문자 매칭

for i in range(1, N):
    prev = start_link[block[i]]
    for j in range(i):
        if block[j] == prev:
            dp[i] = min(dp[i], dp[j]+(i-j)**2)

print(dp[N-1] if dp[N-1] != sys.maxsize else -1)