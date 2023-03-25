# BOJ 12015 가장 긴 증가하는 부분 수열 2
# 시간복잡도 nlog n 으로 해결해야 함 -> dp + 이분탐색
import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

arr =[0]
for i in range(N):
    if A[i] >arr[-1]:
        # 최장 증가 부분 수열 길이와 값 모두 갱신됨
        arr.append(A[i])
    else:
        # bisect로 해당 값이 특정 증가 수열의 끝 값이 최솟값이 되도록 갱신
        arr[bisect_left(arr, A[i])]=A[i]

print(len(arr)-1)



