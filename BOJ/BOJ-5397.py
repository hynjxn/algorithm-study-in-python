import sys
input = sys.stdin.readline

from collections import deque

for _ in range(int(input())):
    passinput = list(input().strip())
    cur_left = deque()
    cur_right = deque()

    for letter in passinput:
        if letter == '<':
            if cur_left:
                cur_right.appendleft(cur_left.pop())
        elif letter == '>':
            if cur_right:
                cur_left.append(cur_right.popleft())
        elif letter == '-':
            if cur_left:
                cur_left.pop()
        else:
            cur_left.append(letter)

    cur_left.extend(cur_right)

    print(''.join(cur_left))