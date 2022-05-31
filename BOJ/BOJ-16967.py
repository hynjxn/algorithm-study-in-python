import sys
input = sys.stdin.readline

H, W, X, Y = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(H+X)]

recover_arr = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H+X):
    for j in range(W+Y):
        if i<X and j<W:
            recover_arr[i][j] = arr[i][j]
        elif i<H and j<Y:
            recover_arr[i][j] = arr[i][j]
        elif i>=X and j>=Y and i<H and j<W:
            recover_arr[i][j] = arr[i][j] - recover_arr[i-X][j-Y]

for i in range(H):
    for j in range(W):
        print(recover_arr[i][j], end=' ')
    print()