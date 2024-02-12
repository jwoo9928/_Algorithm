from collections import deque

m, n = map(int, input().split(" "))
box = []
sortedTomato = []
layer = deque([])
for i in range(n):
    tomatoes = list(map(int, input().split(" ")))
    box.append(tomatoes)
    for j in range(m):
        if tomatoes[j] == 1:
            layer.append((i,j))
sortedTomato.append(layer)

def check_zero(array):
    for row in array:
        if 0 in row:
            return True
    return False


def tomato():
    days = 0
    nextTomatoes = deque([])
    while days < len(sortedTomato) :
        tomatoes = sortedTomato[days]
        if len(tomatoes) <= 0:
            if len(nextTomatoes) > 0:
                sortedTomato.append(nextTomatoes)
            nextTomatoes = deque([])
            days = days+1
            continue
        tx, ty = tomatoes.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = tx + dx, ty + dy
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                nextTomatoes.append((nx, ny))
                box[nx][ny] = 1
    return -1 if check_zero(box) else days-1

print(tomato())