from collections import deque
n = int(input())
houses = [[-1 for _ in range(n)] for _ in range(n)]
graph = []
queue = deque([])
answer = []
for g in range(n):
    graph.append(list(map(int, input())))

def find_house_group(x,y):
    if houses[x][y] == -1 and graph[x][y] == 1:
        queue.append((x,y))
        count = 0
        while queue:
            vx, vy = queue.popleft()
            if houses[vx][vy] == 0:
                continue
            houses[vx][vy] = 0
            count+=1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0,1)]:
                if (0 <= (new_x := vx + dx) < n and 0 <= (new_y := vy + dy) < n
                        and houses[new_x][new_y] == -1
                        and graph[new_x][new_y] == 1):
                    queue.append((vx+dx, vy+dy))
        return count
    return 0


for i in range(n):
    for j in range(n):
        result = find_house_group(i, j)
        if result > 0:
            answer.append(result)

print(len(answer))
answer.sort()
for a in answer:
    print(a)
