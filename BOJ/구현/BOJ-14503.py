# BOJ 14503 로봇청소기
# 0: 북, 1: 동, 2: 남, 3:서
dy = [0, 1, 0,-1]
dx = [-1, 0, 1, 0]
N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

end = False
cnt = 0
while not end:
    if room[r][c] == 0:
        cnt += 1
        room[r][c] = -1
    not_cleaned_nearby = False
    # 주변 4칸에 청소 안 된 칸 있는지 확인
    for i in range(4):
        x, y = r+dx[i], c+dy[i]
        if room[x][y] == 0:
            not_cleaned_nearby = True
            break
    # 청소 안 된 칸 있는 경우
    if not_cleaned_nearby:
        # 반시계 회전
        d = (d-1) % 4
        # 앞 칸이 청소되지 않은 경우 전진
        if room[r+dx[d]][c+dy[d]] == 0:
            r, c = r+dx[d], c+dy[d]
    # 청소 안 된 칸 없는 경우
    else:
        # 한 칸 후진
        r, c = r-dx[d], c-dy[d]
        # 후진 불가능 시 작동 종료
        if room[r][c]==1:
            end = True
print(cnt)

