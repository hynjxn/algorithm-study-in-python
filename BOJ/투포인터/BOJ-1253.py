# BOJ 1253 좋다
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

nums.sort()
cnt = 0

for i in range(N):
    temp = nums[:i]+nums[i+1:]
    left, right = 0, N-2 # 투 포인터 사용
    # left는 오른쪽으로, right는 왼쪽으로 이동
    while left < right:
        temp_sum = temp[left] + temp[right]
        if temp_sum < nums[i]: # 임의 두 개 합이 찾는 값보다 작으면 left 증가
            left += 1
        elif temp_sum > nums[i]: # 임의 두 개 합이 찾는 값보다 크면 right 감소
            right -= 1
        else:
            cnt +=1
            break
print(cnt)