# BOJ 1339 단어 수학
import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
dic = {}
for word in words:
    power = len(word) - 1
    for c in word:
        if c not in dic:
            dic[c] = 10 ** power
        else:
            dic[c] += 10 ** power
        power -= 1

sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
digit = 9
max_sum = 0
for alpha in sorted_dic:
    max_sum += alpha[1]*digit
    digit -= 1

print(max_sum)