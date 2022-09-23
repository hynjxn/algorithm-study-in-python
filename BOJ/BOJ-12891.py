# BOJ 12891 DNA 비밀번호
import sys
from collections import Counter
input = sys.stdin.readline

req= {}
s, p = map(int, input().split())
DNA = input().rstrip()
req['A'], req['C'], req['G'], req['T'] = map(int, input().split())
dic = {'A':0, 'C':0, 'G':0, 'T':0}
cnt = 0

for i in range(s - p + 1):
    valid = True
    if i == 0:
        for j in range(p):
            dic[DNA[j]] += 1
    else:
        dic[DNA[i+p-1]] += 1
        dic[DNA[i-1]] -= 1

    for e in req.keys():
        if req[e] > dic[e]:
            valid = False
            break
    if valid:
        cnt+=1

print(cnt)