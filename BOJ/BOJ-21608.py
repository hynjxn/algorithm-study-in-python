# BOJ 21608 상어 초등학교
import sys
input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
N = int(input())
room = [[0]* (N+1) for _ in range(N+1)]
like = {}

# 1. 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 정함
# 2. 인접한 칸 중 비어있는 칸이 가장 많은 칸
# 3. 행의 번호가 가장 작은 칸
# 4. 열의 번호가 가장 작은 칸

# 자리 배치
for _ in range(N**2):
    arr = list(map(int, input().split()))
    stu, like_stu = arr[0], arr[1:]
    like[stu] = like_stu
    temp = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            if room[i][j]==0:
                adj_like = 0
                adj_empty = 0

                for k in range(4):
                    nr = i+dr[k]
                    nc = j+dc[k]

                    if 1<=nr<N+1 and 1<=nc<N+1:
                        if room[nr][nc] in like_stu:
                            adj_like += 1
                        if room[nr][nc] == 0:
                            adj_empty += 1

                temp.append((adj_like, adj_empty, i, j))

    temp = sorted(temp, key=lambda x: (-x[0], -x[1], x[2], x[3]))
    best_r, best_c = temp[0][2], temp[0][3]
    room[best_r][best_c] = stu

ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        cnt = 0
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]

            if 1 <= nr < N + 1 and 1 <= nc < N + 1:
                if room[nr][nc] in like[room[i][j]]:
                    cnt +=1

        if cnt:
            ans += 10**(cnt-1)

print(ans)

