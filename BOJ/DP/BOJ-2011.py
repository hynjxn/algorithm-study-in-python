# BOJ 2011 암호코드
import sys
input = sys.stdin.readline

pw = input().rstrip()
dp = [0 for _ in range(5001)] # dp[i]: pw i번째 자리 까지 가능한 개수
dp[0], dp[1] = 1, 1 # dp 초기 조건 설정
if pw[0] == '0':
    print(0)
    exit()
else:
    for i in range(2, len(pw)+1):
        two_digit = int(pw[i-2]+pw[i-1])
        # 끝의 자리가 0인 경우에는 0을 따로 암호화 할 수 없으므로
        if int(pw[i-1]) != 0:
            dp[i] += dp[i-1]
        # 끝의 두 자리가 10 ~ 26 사이인 경우
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]

print(dp[len(pw)]%1000000)