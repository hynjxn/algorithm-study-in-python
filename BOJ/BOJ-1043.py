# BOJ 1043
# 집합 연산 사용하여 해결
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
truth = set(map(int, input().split()[1:]))

party = []
ex_party = [0] * M

for _ in range(M):
    party.append(set(map(int, input().split()[1:])))

for _ in range(M):
    # 파티는 동시에 발생한다고 가정함
    # 파티 열릴 때 진실을 아는 사람이 늘어날 수 있으므로 모든 파티를 다시 확인해야 함.
    for i, p in enumerate(party):
        if truth & p: # 해당 파티에 진실을 아는 사람이 있으면
            truth = p | truth # 해당 파티에선 진실을 말해야 하므로 해당 파티 사람들도 진실 아는 사람에 추가됨
            ex_party[i] = '_'

print(ex_party.count(0))