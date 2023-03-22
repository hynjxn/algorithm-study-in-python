# BOJ 14653 너의 이름은
import sys
input = sys.stdin.readline

N, K, Q = map(int, input().split())
people = list(range(2, N+1))
messages = []
all_read = False
for i in range(K):
    R, P = input().split()
    if i == Q-1 and int(R) == 0:
        all_read = True
    messages.append([int(R), ord(P)-64])

if all_read:
    print(-1)
    exit()

for i in range(Q-1, K):
    if messages[i][1] in people:
        people.remove(messages[i][1])

for i in range(Q-1, 0, -1):
    if messages[i][0] == messages[Q][0]:
        if messages[i][1] in people:
            people.remove(messages[i][1])
    else:
        break

for i in people:
    print(chr(i+64), end=' ')



