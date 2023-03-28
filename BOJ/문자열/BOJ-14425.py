# BOJ 14425 문자열 집합
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# list의 삽입, 제거, 탐색, 포함여부 시간복잡도 O(N), set은 O(1)이므로 set을 사용!
s_set = set([input().strip()
             for str in range(N)]) # input의 공백문자 제거 strip()
cnt = 0

for _ in range(M):
    s = input().strip()
    if s in s_set:
        cnt += 1

print(cnt)