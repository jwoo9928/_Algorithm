n = int(input())
arr = set(map(int, input().split(" ")))
m = int(input())
numbers = list(map(int, input().split(" ")))

for num in numbers:
    print(1 if num in arr else 0)