# BOJ 9251 LCS (최장 공통 부분 수열)
# Top-down 사용하는 재귀로 풀이 시 중복 부분 문제 -> 시간 초과
# Bottom-up 방법 사용한 DP 사용해야 함
import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
s1, s2 = ' '+ s1, ' '+ s2 # i, j가 0인 경우를 채워주기 위함. i-1, j-1에서 인덱스 에러 안 나도록
m, n = len(s1), len(s2)

dp = [[0] * n for _ in range(m)]

def lcs(i, j):
    # index 1부터 문자 들어있음
    for i in range(1, m):
        for j in range(1, n):
            if s1[i] == s2[j]:
                # 같은 문자가 나오면 왼쪽 대각선 값에 1 더함
                # 문자열에서 해당 같은 문자 제외하면서 dp 쭉 계산,,,
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # 같은 문자가 아니면 왼쪽, 혹은 위쪽 값
                # 문자열1에서 끝 문자 뺀 것과 문자열2 비교
                # or 문자열2에서 끝 문자 뺀 것과 문자열1 비교
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

lcs(m-1, n-1)
print(dp[m-1][n-1]) # DP 테이블 맨 오른쪽 값이 최장 공통 부분 수열 길이