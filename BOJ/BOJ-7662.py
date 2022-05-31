import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    min_heap = []
    max_heap = []

    k = int(input())
    visited = [False] * k

    for id in range(k):
        letter, n = input().split()
        n = int(n)
        if letter == "I":
            heapq.heappush(min_heap, (n, id))
            heapq.heappush(max_heap, (-n, id))
            visited[id] = True
        if letter == "D":
          if max_heap and n == 1:
            d = heapq.heappop(max_heap)
            min_heap.remove(-d)
          elif min_heap and n == -1:
            d = heapq.heappop(min_heap)
            max_heap.remove(-d)
    if not min_heap:
      print("EMPTY")
    elif len(min_heap)==1:
      x = heapq.heappop(min_heap)
      print(x, x)
    else:
      print(-(heapq.heappop(max_heap)), heapq.heappop(min_heap))
