# BOJ 2841 외계인의 기타 연주
import sys
input = sys.stdin.readline
N, P = map(int, input().split())
# 각 줄의 가장 높은 프렛만 유효 -> stack의 top으로 생각
# 줄 번호 별 스택을 딕셔너리로 묶음
S = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
cnt = 0

for _ in range(N):
    flag = 0
    l, f = map(int, input().split())
    if len(S[l]) < 1 or S[l][-1] < f : # 해당 줄에 누른 프렛 없거나, 현재 누르려는 프렛이 가장 높은 경우 손가락 붙임
        S[l].append(f)
        cnt += 1
    elif S[l][-1] == f: # 해당 줄의 top과 현재 누르려는 프렛 같은 경우 아무 것도 안하고 지나감
        continue
    else:
        while S[l][-1] > f: # 현재 누르려는 프렛이 가장 높아질 때 까지 손가락 하나씩 뗌
            S[l].pop()
            cnt += 1
            if len(S[l]) < 1:
                break
            if S[l][-1] == f: # 만약 현재 누르려는 프렛과 같은 프렛을 이미 누르고 있는 경우 그냥 지나가도록 함
                flag = 1
                break
        if flag == 1: continue
        S[l].append(f)
        cnt += 1
print(cnt)