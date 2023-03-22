# BOJ 26070 곰곰이와 학식
import sys
input = sys.stdin.readline

gom = list(map(int, input().split())) # 곰곰 A, B, C
chong = list(map(int, input().split())) # 총총 X, Y, Z
full_gom = 0

for i in range(3):
    if chong[i] > gom[i]:
        full_gom += gom[i]
        chong[i] = chong[i] - gom[i]
        gom[i] = 0
    else:
        full_gom += chong[i]
        gom[i] = gom[i] - chong[i]
        chong[i] = 0

if gom[0] == gom[1] == gom[2] == 0:
    print(full_gom)
    exit()
for _ in range(3):
    for i in range(3):
        if chong[i] == 0:
            continue
        if gom[i] == 0 and chong[i] != 0:
            temp = chong[i] % 3
            if i==2:
                j = 0
            else:
                j = i+1
            chong[j] += chong[i]//3
            chong[i] = temp
        if gom[i] !=0 and chong[i] != 0:
            if chong[i] > gom[i]:
                full_gom += gom[i]
                chong[i] = chong[i] - gom[i]
                gom[i] = 0
            else:
                full_gom += chong[i]
                gom[i] = gom[i] - chong[i]
                chong[i] = 0


print(full_gom)


