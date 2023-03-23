# BOJ 9465 스티커
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    sticker=[]
    dp = [[0]*2 for _ in range(n+1)]
    for _ in range(2):
        sticker.append([0]+list(map(int, input().split())))
    sticker = list(zip(*sticker))
    dp[1][0] ,dp[1][1] = sticker[1][0], sticker[1][1]
    for i in range(2, n+1):
        dp[i][1]=max(dp[i-1][0], dp[i-2][0])+sticker[i][1]
        dp[i][0] = max(dp[i - 1][1], dp[i - 2][1]) + sticker[i][0]
    print(max(dp[n]))