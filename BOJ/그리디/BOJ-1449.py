# BOJ 1449 수리공 항승
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
leak = list(map(int, input().split()))
leak.sort()
start = leak[0] - 0.5
count = 1

for t in leak[1:]:
    if start+L >= t + 0.5:
        continue
    else:
        start = t - 0.5
        count += 1

print(count)