# BOJ 17951 흩날리는 시험지 속에서 내 평점이 느껴진거야
import sys
from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())
paper = list(map(int, input().split()))

l, r = 0, sum(paper)+1
ans = 0
while l<=r:
    mid = (l+r) // 2
    min_score = 0
    group = 0
    for p in paper:
        min_score += p
        if min_score>=mid:
            group +=1
            min_score = 0

    if group >= K:
        ans = mid
        left = mid+1
    else:
        right = mid - 1

print(ans)
