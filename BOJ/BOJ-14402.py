import sys
input = sys.stdin.readline

N = int(input())
check = {}
cnt = 0

for _ in range(N):
    s, p = input().rstrip().split()
    if s not in check:
        if p == '+':
            check[s] = 1 # 정상 출근
        else:
            cnt += 1 # 들어간 기록 없는데 나온 기록만 있는 경우
    else:
        if p == '+':
            check[s] += 1 # 이름 같은 사람이 출근함
        else:
            if check[s] != 0:
                check[s] -= 1 # 퇴근
            else:
                cnt += 1 # 값 0 이면 이미 퇴근 처리 된 것임

cnt += sum(check.values())
print(cnt)