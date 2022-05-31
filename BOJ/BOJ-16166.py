import sys
input = sys.stdin.readline

visited=[0]
N = int(input())


h = {}
route = {}
for x in range(1,N+1):
    l = list(map(int, input().split()))
    for y in l[1:]: # {역: 호선}
        if h.get(y):
            h[y].extend([x])
        else:
            h[y]=list()
            h[y].extend([x])
        if route.get(y):
            route[y].extend(l[1:])
        else:
            route[y]=l[1:]
dest = int(input())

def dfs(start, dest, cnt):
    way = []
    for i in route[start]:
        if i == dest:
            return cnt
        if len(h[i]==1): # 환승역 아닌 곳
            visited.append(i)
        else:
            if i not in visited:
                visited.append(i)
                way.append(i)
        for x in way:
            return dfs(x, dest, cnt+1)

c = dfs(0, dest, 0)

if c==None:
    print(-1)
else:
    print(c)