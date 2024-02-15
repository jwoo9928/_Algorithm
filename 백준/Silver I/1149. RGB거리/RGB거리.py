import sys

n = int(sys.stdin.readline())
rgb = []
dp = [[0 for _ in range(3)] for _ in range(n)]
for i in range(n):
    inp = list(map(int, input().split()))
    if i == 0:
        dp[0] = inp
    rgb.append(inp)

for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][j] = rgb[i][j] + min(dp[i - 1][1], dp[i - 1][2])
        if j == 1:
            dp[i][j] = rgb[i][j] + min(dp[i - 1][0], dp[i - 1][2])
        if j == 2:
            dp[i][j] = rgb[i][j] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[n-1]))