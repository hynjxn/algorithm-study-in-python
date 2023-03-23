# BOJ 2075 N번째 큰 수
# 크기 N 만큼의 최소 힙을 유지
import sys
import heapq
input = sys.stdin.readline

N = int(input())
# 각 행의 길이가 N. 첫 행을 그대로 최소 힙으로 만들어 사용
heap = list(map(int, input().split()))
heapq.heapify(heap)

for _ in range(1, N):
    nums = list(map(int, input().split()))
    for num in nums:
        if num > heap[0]: # 힙의 최소 원소보다 num이 큰 경우 최소 원소를 pop하고 num을 push
            heapq.heappop(heap)
            heapq.heappush(heap, num)

# 모든 수를 탐색 한 후 N 크기의 힙에서 가장 작은 원소가 N번째 큰 수
print(heap[0])