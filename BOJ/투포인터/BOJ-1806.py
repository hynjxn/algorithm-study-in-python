# BOJ 1806 부분합
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int,input().split()))

sub_tot, min_len = 0, 100001
l, r = 0, 0

while l <= r <= N:
    if sub_tot >= S:
        min_len = min(min_len, r-l)
        sub_tot -= arr[l]
        l += 1
    else:
        if r == N:
            break
        sub_tot += arr[r]
        r += 1

if min_len == 100001:
    print(0)
else:
    print(min_len)