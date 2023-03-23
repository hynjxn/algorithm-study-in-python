# BOJ 2096 내려가기
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
max_t, min_t = arr, arr

for _ in range(1, N):
    arr = list(map(int, input().split()))
    max_t = [arr[0]+max(max_t[0], max_t[1]), arr[1]+max(max_t[0], max_t[1], max_t[2]),
             arr[2]+max(max_t[1], max_t[2])]
    min_t = [arr[0] + min(min_t[0], min_t[1]), arr[1] + min(min_t[0], min_t[1], min_t[2]),
             arr[2] + min(min_t[1], min_t[2])]

print(max(max_t), min(min_t))