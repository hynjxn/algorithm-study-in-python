import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
nums = list(map(int, input().split()))
nums.sort()

left, right = 0, N-1
cnt = 0
while left < right:
    temp = nums[left]+nums[right]
    if temp == M:
        cnt += 1
        left += 1
        right -=1
    elif temp < M:
        left += 1
    else:
        right -= 1

print(cnt)