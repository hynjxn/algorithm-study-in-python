# deque을 이용한 풀이
from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())
    cards = deque(input().split())
    # 맨 앞 카드를 덱에 넣고 시작
    ans = deque(cards.popleft())

    # 덱의 맨 앞 카드보다 작으면 왼쪽, 아니면 오른쪽으로 append.
    while cards:
        char = cards.popleft()
        if char <= ans[0]:
            ans.appendleft(char)
        else:
            ans.append(char)

    print(''.join(ans))