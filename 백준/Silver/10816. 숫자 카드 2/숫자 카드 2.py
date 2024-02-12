from collections import Counter

n = int(input())
arr = list(map(int, input().split(" ")))
arrSet = set(arr)
counter = Counter(arr)
m = int(input())
numbers = list(map(int, input().split(" ")))

for n in numbers:
    result = counter.get(n)
    print(result if result != None else 0, end=' ')
