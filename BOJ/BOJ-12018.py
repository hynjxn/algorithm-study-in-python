import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

min_heap = []

for _ in range(N):
    p, l = map(int, input().split())
    mileage= list(map(int,input().split()))
    heapq.heapify(mileage)
    if (p - l) >=0:
        for _ in range(p - l + 1):
            min_mile = heapq.heappop(mileage)
        heapq.heappush(min_heap, min_mile)
    else:
        heapq.heappush(min_heap, 1)
num = 0

while M > 0:
    M -= heapq.heappop(min_heap)
    if M < 0:
        break
    num +=1
    if not min_heap:
        break

print(num)
