import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(n+1)] # 회수를 저장

def min_cal(): #바텀 업
    for i in range(2, n+1):

        dp[i] = dp[i-1] + 1 #1을 추가
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
    print(dp[n])

min_cal()