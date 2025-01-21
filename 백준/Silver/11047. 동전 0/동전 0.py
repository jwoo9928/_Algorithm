n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)

count = 0
for coin in coins:
    if k >= coin:
        count += k // coin
        k = k % coin
print(count)