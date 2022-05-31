import sys
input = sys.stdin.readline

str = input().rstrip()
tag = False

word = ""
ans = ""

for c in str:
    if tag == False:
        if c == "<":
            tag = True
            word = word + c
        elif c == " ": # 단어 공백으로 구분
            word = word + c
            ans = ans + word
            word = ""
        else:
            word = c + word # 문자열 덧셈 유의.
    else:
        word = word + c
        if c == ">":
            tag = False
            ans = ans + word
            word = ""

print(ans+word)