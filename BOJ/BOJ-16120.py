import sys
input = sys.stdin.readline

str = input().rstrip()
ppap = ['P','P','A','P']
stack = []

for c in str:
    stack.append(c)
    if stack[-4:] == ppap:
        for _ in range(3): stack.pop() # ppap -> p로 변환

if stack == ppap or stack == ['P']:
    print("PPAP")
else:
    print("NP")
