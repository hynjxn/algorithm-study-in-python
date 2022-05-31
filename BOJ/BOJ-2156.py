import sys
input = sys.stdin.readline

N = int(input())
wine = [int(input()) for _ in range(N)]

dp = [0]
# 초기 조건 설정 2잔까지는 두잔 다 먹는게 최대
dp.append(wine[0])
if N > 1:
    dp.append(wine[0]+wine[1])
# 1) 이번 포도주 먹고 앞 포도주 안먹음 2) 이번 포도주 먹고 전 포도주도 먹음 3) 이번 포도주 안먹음

for i in range(3, N+1):
    # wine[0]이 첫잔이므로 현재 잔은 wine[i-1]임
    dp.append(max(dp[i-2]+wine[i-1], dp[i-3]+wine[i-2]+wine[i-1], dp[i-1]))

print(dp[N])