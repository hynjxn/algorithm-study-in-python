# BOJ 2504 괄호의 값
import sys
input = sys.stdin.readline

bracket = input().rstrip()
tmp = 1
res = 0
stack = []

for i, br in enumerate(bracket):
    if br == "(":
        stack.append(br)
        tmp *= 2
    elif br == "[":
        stack.append(br)
        tmp *= 3

    elif br == ")":
        if not stack or stack[-1] == "[":
            print(0)
            exit(0)
        if bracket[i-1] == "(":
            res += tmp
        stack.pop()
        tmp //=2
    elif br == "]":
        if not stack or stack[-1] == "(":
            print(0)
            exit(0)
        if bracket[i - 1] == "[":
            res += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(res)
