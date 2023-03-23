# BOJ 3078 좋은 친구
# 슬라이딩 윈도우
import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())
dic = defaultdict(int)
friends = [len(input().rstrip()) for _ in range(N)]
cnt = 0

for i in range(N):
    if i > K:
        dic[friends[i-K-1]] -= 1
    # 같은 길이 이름의 친구가 윈도우에 존재할 때 카운트 먼저 하고, 윈도우에 추가시켜야 함!
    cnt += dic[friends[i]]
    dic[friends[i]] += 1

print(cnt)