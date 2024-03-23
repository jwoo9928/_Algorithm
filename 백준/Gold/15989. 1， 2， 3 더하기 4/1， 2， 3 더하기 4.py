n = int(input())
dp = [[0 for _ in range(4)] for _ in range(10001)]

# 초기값 설정
dp[1][1] = 1
dp[2][1], dp[2][2] = 1, 1
dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1

for i in range(4, 10001):
    dp[i][1] = dp[i - 1][1]
    dp[i][2] = dp[i - 2][1] + dp[i - 2][2]
    dp[i][3] = dp[i - 3][1] + dp[i - 3][2] + dp[i - 3][3]

for _ in range(n):
    t = int(input().strip())
    print(dp[t][1] + dp[t][2] + dp[t][3])