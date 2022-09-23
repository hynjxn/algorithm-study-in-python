# BOJ 1911 흙길 보수하기
import sys
import math
input = sys.stdin.readline

N, L = map(int, input().split())
pools = []
for _ in range(N):
    pools.append(tuple(map(int, input().split())))
pools.sort(key = lambda x:(x[0], x[1]))

cnt = 0
endIndex = 0
for start, end in pools:
    if endIndex < start:
        p = math.ceil((end-start) / L)
        cnt += p
        endIndex = start + (L * p)
    else:
        p = math.ceil((end - endIndex) / L)
        cnt += p
        endIndex += L * p

print(cnt)

