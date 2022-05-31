import sys
input = sys.stdin.readline

# 아직 안 지난 곳 0, 사과 1, 지나간 곳 2
# 우회전 상0 -> 우1 -> 하2 -> 좌3 -> 상 -> ...
# 좌회전 상0 -> 좌3 -> 하2 -> 우1 -> 상 -> ...

def rotation(d, c):
    if c =="L":
        d = (d-1) % 4
    else:
        d = (d+1) % 4

N = int(input())
matrix = [[0] * N for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for _ in range(int(input())):
    i, j = map(int, input().split())
    matrix[i-1][j-1] = 1 # 사과 저장

rotate = {}
for _ in range(int(input())):
    x, c = input.split()
    rotate[int(x)] = c

