import sys
input = sys.stdin.readline

bracket = input().rstrip()

stack1 = [] # (를 담는 스택
stack2 = [] # stack1이 비었을 때 )를 담는 스택. 회생 불가능한 )

for c in bracket:
    if c == "(":
        stack1.append(c)
    elif not stack1:
        stack2.append(c)
    else:
        stack1.pop()

print(len(stack1)+len(stack2))
