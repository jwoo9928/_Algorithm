import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

min_height = 0
max_height = max(trees)
result = 0

while min_height <= max_height:
    mid_height = (min_height + max_height) // 2
    total_take = 0

    for tree in trees:
        if tree > mid_height:
            total_take += tree - mid_height

    if total_take >= m:
        result = mid_height
        min_height = mid_height + 1
    else:
        max_height = mid_height - 1

print(result)
