#BOJ 15685 드래곤 커브
import sys
input = sys.stdin.readline

N = int(input())
# 좌표 중복 처리
curves = set()
# 90도 회전 시 방향
next = {0: 1, 1: 2, 2: 3, 3: 0}
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    curves.add((x, y))
    curves.add((x+dx[d], y+dy[d]))
    stack = [d]
    now = (x+dx[d], y+dy[d])
    for _ in range(g):
        next_stack = [] # 현재 세대의 방향정보
        for i in range(len(stack), 0, -1):
            # 전세대 까지의 방향 정보를 끝점에서부터 가져옴
            w = next[stack[i-1]]
            now = (now[0] + dx[w], now[1] + dy[w])
            curves.add(now)
            next_stack.append(w)
        stack += next_stack # 현재 세대 스택에 저장
cnt = 0
for x, y in curves:
    if (x+1, y) in curves and (x, y+1) in curves and (x+1, y+1) in curves:
        cnt += 1


print(cnt)





