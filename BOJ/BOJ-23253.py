import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dummies = []
result = True

for _ in range(M):
    ki = int(input())
    dummy = list(map(int, input().split()))
    if dummy != sorted(dummy, reverse=True):
        result = False
        break

if result:
    print("Yes")
else:
    print ("No")
