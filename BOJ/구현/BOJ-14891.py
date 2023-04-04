#BOJ 14891 톱니바퀴
from collections import deque
wheel = [deque(input().rstrip()) for _ in range(4)] # N극 0, S극 1
K = int(input())
arr = [list(map(int, input().split())) for _ in range(K)]

def turn(i, d):
    if d==-1:
        wheel[i].append(wheel[i].popleft())
    elif d==1:
        wheel[i].appendleft(wheel[i].pop())

for i, d in arr:
    i -= 1
    turn_index = deque([[i,d]])
    if i != 0: # 왼쪽 탐사
        for j in range(i,0,-1):
            if wheel[j][6] != wheel[j-1][2]:
                if (i-(j-1))%2 == 0:
                    turn_index.append([j-1, d])
                else:
                    turn_index.append([j-1, -d])
            else:
                break

    if i != 3: # 오른쪽 탐사
        for j in range(i,3):
            if wheel[j][2] != wheel[j+1][6]:
                if (i-(j+1))%2 == 0:
                    turn_index.append([j+1, d])
                else:
                    turn_index.append([j+1,-d])
            else:
                break
    # if i==0:
    #     if wheel[0][2] != wheel[1][6]:
    #         turn_index.append([1,-d])
    #         if wheel[1][2] != wheel[2][6]:
    #             turn_index.append([2,d])
    #             if wheel[2][2] != wheel[3][6]:
    #                 turn_index.append([3,-d])
    # elif i==1:
    #     if wheel[1][6] != wheel[0][2]:
    #         turn_index.append([0,-d])
    #     if wheel[1][2] != wheel[2][6]:
    #         turn_index.append([2,-d])
    #         if wheel[2][2] != wheel[3][6]:
    #             turn_index.append([3,d])
    # elif i==2:
    #     if wheel[2][2] != wheel[3][6]:
    #         turn_index.append([3, -d])
    #     if wheel[2][6] != wheel[1][2]:
    #         turn_index.append([1, -d])
    #         if wheel[1][6] != wheel[0][2]:
    #             turn_index.append([0, d])
    # elif i==3:
    #     if wheel[3][6] != wheel[2][2]:
    #         turn_index.append([2,-d])
    #         if wheel[2][6] != wheel[1][2]:
    #             turn_index.append([1,d])
    #             if wheel[1][6] != wheel[0][2]:
    #                 turn_index.append([0,-d])
    while turn_index:
        idx, di = turn_index.popleft()
        turn(idx, di)
score = 0
for i in range(4):
    score += int(wheel[i][0])*(2**i)
print(score)