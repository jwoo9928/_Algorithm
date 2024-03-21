import sys
from collections import deque

R, C, N = map(int, sys.stdin.readline().split())

bomMap = [list(input().rstrip()) for _ in range(R)]
q = deque()

def pop():
    while q:
        x, y = q.popleft()
        bomMap[x][y] = '.'
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and bomMap[nx][ny] == 'O':
                bomMap[nx][ny] = '.'

def task(t):
    if t % 2 == 0:
        for i in range(R):
            for j in range(C):
                if bomMap[i][j] == '.':
                    bomMap[i][j] = 'O'
    elif t % 2 == 1 and t != 1:
        pop()
        for i in range(R):
            for j in range(C):
                if bomMap[i][j] == 'O':
                    q.append((i, j))

for i in range(R):
    for j in range(C):
        if bomMap[i][j] == 'O':
            q.append((i, j))

for t in range(2, N + 1):
    task(t)

for row in bomMap:
    print(''.join(row))
