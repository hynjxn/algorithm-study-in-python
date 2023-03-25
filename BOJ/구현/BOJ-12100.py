# BOJ 2048 (Easy)
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
input_board = [list(map(int, input().split())) for _ in range(N)]

# 어차피 빈칸은 땡겨지게 되어 있음 -> 0 제거한 리스트 추출하여 이동시키고 끝에 0 추가
def move(board, d):
    if d == 0:
        for r in range(N):
            arr = board[r]
            q = deque([arr[i] for i in range(N) if arr[i]])
            temp = []
            while q:
                num = q.popleft()
                if not q:
                    temp.append(num)
                    break
                if num == q[0]:
                    num += q.popleft()
                temp.append(num)
            while len(temp) < N:
                temp.append(0)
            board[r] = temp

    elif d==1:
        for r in range(N):
            arr = board[r][::-1]
            q = deque([arr[i] for i in range(N) if arr[i]])
            temp = []
            while q:
                num = q.popleft()
                if not q:
                    temp.append(num)
                    break
                if num == q[0]:
                    num += q.popleft()
                temp.append(num)
            while len(temp) < N:
                temp.append(0)
            board[r] = temp[::-1]

    elif d==2:
        for c in range(N):
            arr = list(zip(*board))[c]
            q = deque([arr[i] for i in range(N) if arr[i]])
            temp = []
            while q:
                num = q.popleft()
                if not q:
                    temp.append(num)
                    break
                if num == q[0]:
                    num += q.popleft()
                temp.append(num)
            while len(temp) < N:
                temp.append(0)
            for i in range(N):
                board[i][c] = temp[i]

    elif d==3:
        for c in range(N):
            arr = list(zip(*board))[c][::-1]
            q = deque([arr[i] for i in range(N) if arr[i]])
            temp = []
            while q:
                num = q.popleft()
                if not q:
                    temp.append(num)
                    break
                if num == q[0]:
                    num += q.popleft()
                temp.append(num)
            while len(temp) < N:
                temp.append(0)
            for i in range(N):
                board[i][c] = temp[-i-1]
    return board

def find_biggest(cnt, board):
    global max_block
    if cnt==5:
        max_block = max(max_block, max(map(max, board)))
        return
    for i in range(4):
        find_biggest(cnt+1, move(deepcopy(board), i))
max_block = 0
find_biggest(0, input_board)
print(max_block)

