# BOJ 1477 휴게소 세우기
import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
arr = [0] + sorted(list(map(int, input().split()))) + [L]

l, r = 1, L-1
res = 0

while l <= r:
    cnt = 0
    mid = (l + r) // 2 # 휴게소 사이 구간의 최대값
    for i in range(1, len(arr)):
        section = arr[i] - arr[i-1]
        if section > mid:
            cnt += (section - 1) // mid # 세워야 하는 휴게소 개수
    if cnt > M:
        l = mid + 1
    else:
        r = mid - 1
        res = mid

print(res)