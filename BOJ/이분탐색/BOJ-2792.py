# BOJ 2792 보석상자
# 보석 못 받는 사람 있어도 상관 없음. 근데 보석은 남으면 안 됨
import sys
import math
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N, M = map(int, input().split())
gem = []
for _ in range(M):
    num = int(input())
    gem.append(num)

l, r = 1, max(gem)
jealous = 0
while l <= r: # 질투심의 크기를 이분 탐색
    mid = (l+r) // 2
    tmp = 0 # 필요한 사람의 수
    for i in gem:
        tmp += math.ceil(i / mid)
    if tmp > N: # 보석이 남은 경우
        l = mid + 1
    else:
        r = mid - 1
        jealous = mid

print(jealous)