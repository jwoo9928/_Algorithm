import sys

n = int(sys.stdin.readline())
tr = []
dp = []
for i in range(n):
    numbers = list(map(int, input().split()))
    tr.append(numbers)
    dp.append([0 for _ in range(len(numbers))])

dp[0][0] = tr[0][0]
for i in range(1, n):
    numbers = tr[i]
    for j in range(len(numbers)):
        if j - 1 >= 0 :
            dp[i][j] = max(dp[i][j], numbers[j] + dp[i-1][j-1])
        if j < len(tr[i-1]):
            dp[i][j] = max(dp[i][j], numbers[j] + dp[i-1][j])

print(max(dp[n-1]))
