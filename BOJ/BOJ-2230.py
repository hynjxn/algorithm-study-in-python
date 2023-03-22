# BOJ 2230 수 고르기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))
A.sort()
l, r = 0, 0
ans = 987654321
while l <= r < N:
    temp = A[r]-A[l]
    if temp == M:
        print(M)
        exit(0)
    if temp < M:
        r += 1
    else:
        ans = min(ans, temp)
        l += 1

print(ans)

