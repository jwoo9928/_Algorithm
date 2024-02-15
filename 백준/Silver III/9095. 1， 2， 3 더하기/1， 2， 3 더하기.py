import sys

n = int(sys.stdin.readline())
numbers = []
for i in range(n):
    numbers.append(int(sys.stdin.readline()))
maxValue = max(numbers)
dp = [0 for _ in range(maxValue+1)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, maxValue + 1):
    if i -1 > 0:
        dp[i] += dp[i - 1]
    if i - 3 > 0:
        dp[i] += dp[i - 3]
    if i - 2 > 0:
        dp[i] += dp[i - 2]


for num in numbers:
    print(dp[num])