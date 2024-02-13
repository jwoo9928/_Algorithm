import sys

k, n = map(int, sys.stdin.readline().split())
lines = []
for i in range(k):
    lines.append(int(input()))

def find_lines():
    standard = max(lines)
    minL = 1
    maxL = standard
    maxLine = 0
    while minL <= maxL:
        result = 0
        standard = (minL+maxL) // 2
        for line in lines:
            result += line//standard
        if result >= n:
            if standard > maxLine:
                maxLine = standard
            minL = standard + 1
        else:
            maxL = standard-1
    return maxLine


print(find_lines())


