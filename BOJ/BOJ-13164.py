# BOJ 13164 행복유치원
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

gap = []
for i in range(1, N):
    gap.append(arr[i]-arr[i-1])
gap.sort()
print(gap)
cost = 0
for i in range(N-K):
    cost += gap[i]

print(cost)