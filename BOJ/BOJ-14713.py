import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
S = []
for _ in range(N):
    S.append(deque(input().split()))
L = deque(input().split())


while L:
    flag = 0
    for i in range(N):
        if not S[i]: continue
        if L[0] == S[i][0]:
            L.popleft()
            S[i].popleft()
            flag = 1
            break
    if flag == 0:
        break

if not L:
    for i in range(N):
        if S[i]:
            print("Impossible")
            exit()
    print("Possible")
else:
    print("Impossible")