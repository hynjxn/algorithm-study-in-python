# BOJ 11723 집합
import sys
input = sys.stdin.readline

S = 0
M = int(input())
for _ in range(M):
    arr = list(input().split())
    if len(arr) == 2:
        arr[1] = int(arr[1])
    if arr[0] == "all":
        S = (1<<21) -1
    elif arr[0] == "empty":
        S = 0
    elif arr[0] == "add":
        S |= (1<<arr[1])
    elif arr[0] == "remove":
        S &= ~(1<<arr[1])
    elif arr[0] == "check":
        if (S & (1<<arr[1])):
            print(1)
        else:
            print(0)
    elif arr[0] == "toggle":
        S ^= (1<<arr[1])