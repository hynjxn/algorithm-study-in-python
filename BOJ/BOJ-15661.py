# BOJ 15661 링크와 스타트

import sys
from itertools import combinations
input = sys.stdin.readline
arr = []
N = int(input())

for _ in range(N):
    arr.append(list(map(int,input().split())))

def sum_power(l):
    res = 0
    for i in range(len(l)):
        for j in range(len(l)):
            res += arr[l[i]][l[j]]
    return res

min_gap = 987654321
#for i in range(1, N//2 +1):



# 비트마스킹. 0이면 스타트팀 1이면 링크팀
# 각 팀당 인원 1명씩은 필요. 0...01부터 1...10까지
for i in range(1, (1<<N)-1):
    start = []
    link = []
    for j in range(N):
        if (i & (1<<j) == 0):
            start.append(j)
        else:
            link.append(j)
    min_gap = min(min_gap, abs(sum_power(start)-sum_power(link)))

print(min_gap)

