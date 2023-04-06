# BOJ 15686 치킨 배달
from itertools import combinations
N, M = map(int, input().split())
home, chicken = [], []

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            home.append((i, j))
        elif temp[j] == 2:
            chicken.append((i, j))
# 조합 직접 구현하여 사용
def combination(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i + 1:], n - 1):
            result.append([elem] + rest)
    return result

min_city_chic_dist = float('inf')
for comb in combination(chicken, M):
    city_chic_dist = 0
    for h_i, h_j in home:
        chicken_dist = float('inf')
        for c_i, c_j in comb:
            chicken_dist = min(abs(c_i-h_i)+abs(c_j-h_j), chicken_dist)
        city_chic_dist += chicken_dist
    min_city_chic_dist = min(city_chic_dist, min_city_chic_dist)

print(min_city_chic_dist)

