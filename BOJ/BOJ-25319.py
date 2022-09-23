# 안해 샹
import sys
from collections import deque

input = sys.stdin.readline

N, M, S_len = map(int, input().split())
dungeon = [list(input().rstrip()) for _ in range(N)]
s = input().rstrip()
S = deque(s)
L = ""
cnt = 0
i, j = 0, 0
while 1:
    if len(S) == 0:
        cnt += 1
        S = deque(s)
    if i == N-1 and j == M-1 and (len(S)==0 or "".join(list(S))==s):
        break
    if len(S) != 0:
        # 현재 위치에서 P하면 되는 경우
        if dungeon[i][j] == S[0]:
            S.popleft()
            L += "P"
            dungeon[i][j] = '_'
            if len(S) == 0:
                continue
        # 아래쪽으로 가는 경우
        if i+1 < N and dungeon[i+1][j] == S[0]:
            i = i+1
            L += "D"
            continue
        # 오른쪽으로 가는 경우
        elif j+1 < M and dungeon[i][j+1] == S[0]:
            j = j+1
            L += "R"
            continue
        # 위쪽으로 가는 경우
        elif i-1 >= 0 and dungeon[i-1][j] == S[0]:
            i = i-1
            L += "U"
            continue

        # 왼쪽으로 가는 경우
        elif j-1 >= 0 and dungeon[i][j-1] == S[0]:
            j = j-1
            L += "L"
            continue
    # 아래쪽으로 가는 경우
    if i + 1 < N and dungeon[i+1][j] !="_":
        i = i + 1
        L += "D"
        continue
    # 오른쪽으로 가는 경우
    elif j + 1 < M and dungeon[i][j+1] !="_":
        j = j + 1
        L += "R"
        continue
    # 위쪽으로 가는 경우
    elif i - 1 >= 0 and dungeon[i-1][j] !="_":
        i = i - 1
        L += "U"
        continue
    # 왼쪽으로 가는 경우
    elif j - 1 >= 0 and dungeon[i][j-1] !="_":
        j = j - 1
        L += "L"
        continue
print(cnt, len(L))
print(L)