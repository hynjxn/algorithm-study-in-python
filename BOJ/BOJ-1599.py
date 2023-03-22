#BOJ 1599 민식어
import sys
from functools import cmp_to_key
input = sys.stdin.readline
minsik = {'a': 1, 'b':2, 'k':3, 'd':4, 'e':5, 'g':6, 'h':7, 'i':8, 'l':9, 'm':10, 'n':11,
           'ng':12, 'o':13, 'p':14, 'r':15, 's':16, 't':17, 'u':18, 'w':19, 'y':20}
N = int(input())
words = []
for _ in range(N):
    w = input().rstrip()
    word = []
    for i in range(len(w)):
        if i!= len(w)-1 and w[i]=='n' and w[i+1]=='g':
            word.append('ng')
        elif i!=0 and w[i-1]=='n' and w[i]=='g':
            continue
        else:
            word.append(w[i])
    words.append(word)

def customSort(a, b):
    n = min(len(a), len(b))
    for i in range(n):
        if minsik[a[i]]< minsik[b[i]]:
            return -1
        elif minsik[a[i]]>minsik[b[i]]:
            return 1
    if len(a) <len(b):
        return -1
    else:
        return 1

res = sorted(words, key=cmp_to_key(customSort))
for word in res:
    print(''.join(c for c in word))
