# BOJ 10775 공항 (유니온파인드)
import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
gate=[i for i in range(G+1)]

def dock(x):
    if x == gate[x]:
        return x
    gate[x] = dock(gate[x])
    return gate[x]
ans = 0
for _ in range(P):
    plane_gate = int(input())
    x = dock(plane_gate)
    if x:
        ans += 1
        gate[x] = dock(x-1)
    else:
        break
print(ans)