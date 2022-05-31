import sys
input = sys.stdin.readline

res = 0
N = int(input())
stack = [] # (height, count)의 튜플. 같은 키의 사람들 끼리는 서로 다 볼수 있기 때문에 count 추가
for _ in range(N):
    h = int(input())
    while stack and stack[-1][0] < h:
        res += stack.pop()[1]
    if not stack:
        stack.append((h,1))
        continue

    if stack[-1][0] == h:
        cnt = stack.pop()[1]
        res += cnt

        if stack: # 지금의 top과 현재 사람 서로 볼 수 있음
            res +=1
        stack.append((h,cnt+1))
    else:
        stack.append((h,1))
        res +=1
print(res)