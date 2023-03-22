# BOJ 2877 4와 7
import sys
import math
input = sys.stdin.readline

K = int(input())
print(bin(K+1))
# # 2의 등비수열 식 -> 2**(n+1)-2
# x= math.ceil(math.log2(K+2)-1)
# ptr = K - (2**x - 2)
# # zfill -> x자리의 이진수로 변환
# bi = format(ptr-1, 'b').zfill(x)
# bi_to_47 = bi.replace('0','4').replace('1','7')
# print(bi_to_47)