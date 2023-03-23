# BOJ 2473 세 용액
# pypy는 통과, python은 시간초과
import sys
input = sys.stdin.readline
N = int(input())
sol = list(map(int, input().split()))
sol.sort()

near_zero = 9876543210
res = []
# 한 개는 고정시키고 투 포인터 돌리는 방식
for i in range(N-2):
    l, r = i + 1, N - 1
    while l < r:
        temp = sol[i] + sol[l] + sol[r]
        if abs(temp) < abs(near_zero):
            near_zero = temp
            res = [sol[i], sol[l], sol[r]]
        if temp == 0:
            print(*res)
            exit()
        elif temp < 0:
            l += 1
        else:
            r -= 1
print(*res)

