# BOJ 1024
import sys
input = sys.stdin.readline

N, L = map(int, input().split())

# N = x + (x+1) + ... + (X+i-1) = i*x + i(i-1)/2
# ix = N - i(i-1)/2 이고, x는 정수이므로 해당 식이 i로 나누어 떨어지는 i를 찾는다.
for i in range(L, 101):
    c = N  - (i * (i - 1)) / 2
    if c < 0: # x가 음이 아닌 정수
        print(-1)
        exit()
    if c % i == 0:
        x = c // i
        for j in range(i):
            print(int(x+j), end=' ')
        exit()

print(-1)

