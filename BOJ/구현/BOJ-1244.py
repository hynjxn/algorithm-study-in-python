# BOJ 1244 스위치 켜고 끄기
import sys
input = sys.stdin.readline

N = int(input())
switch = list(map(int,input().rstrip().split()))

stu = int(input())

for _ in range(stu):
    x, y = map(int, input().split())
    if x == 1:

        for i in range(N // y):
            idx = (y * (i + 1)) - 1
            if switch[idx] == 0: switch[idx] = 1
            elif switch[idx] == 1: switch[idx] = 0
    elif x == 2:
        idx = y - 1
        if switch[idx] == 0: switch[idx] = 1
        elif switch[idx] == 1: switch[idx] = 0
        left = idx - 1
        right = idx + 1

        while left >= 0 and right < N and switch[left] == switch[right]:
            if switch[left] == 0:
                switch[left], switch[right] = 1, 1
            elif switch[left] == 1:
                switch[left], switch[right] = 0, 0
            left -= 1
            right += 1
            if left < 0 or right >= N: break

for i in range(N):
    print(switch[i], end=" ")
    if (i+1) % 20 == 0:
        print()
