# BOJ 8972 미친 아두이노
import sys
input = sys.stdin.readline

R, C = map(int, input().split())

crazy = set()
d = {'1':(1, -1), '2':(1, 0), '3':(1, 1), '4':(0, -1), '5':(0, 0), '6':(0, 1), '7':(-1, -1), '8':(-1, 0), '9':(-1, 1)}
for i in range(R):
    temp = list(input().rstrip())
    for j in range(C):
        if temp[j] == 'I':
            jongsu = [i, j]
        elif temp[j] == 'R':
            crazy.add((i, j))
s = list(input().rstrip())

for i in range(len(s)):
    # 종수
    dx, dy = d[s[i]]
    jongsu[0] += dx
    jongsu[1] += dy
    if (jongsu[0], jongsu[1]) in crazy:
        print("kraj "+str(i+1))
        exit()

    bomb = set()
    next = set()
    for x, y in crazy:
        min_gap = 9999
        dx, dy = 0, 0
        for c_dx, c_dy in d.values():
            gap = abs(jongsu[0]-x-c_dx) + abs(jongsu[1]-y-c_dy)
            if gap < min_gap:
                min_gap = gap
                dx, dy = c_dx, c_dy
        x += dx
        y += dy
        if [x, y] == jongsu:
            print("kraj " + str(i+1))
            exit()
        if (x, y) in next:
            bomb.add((x, y))
        else:
            next.add((x, y))
    for x, y in bomb:
        next.remove((x,y))
    crazy = next

board = [['.' for _ in range(C)] for _ in range(R)]
for x, y in crazy:
    board[x][y]='R'
board[jongsu[0]][jongsu[1]]='I'
for r in board:
    print(''.join(r))