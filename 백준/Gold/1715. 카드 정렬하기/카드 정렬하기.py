import heapq

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)
result = 0

while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    result += a + b
    heapq.heappush(cards, a + b)
print(result)
