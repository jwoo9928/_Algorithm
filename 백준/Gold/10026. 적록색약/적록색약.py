import sys

sys.setrecursionlimit(10000)
RGBGraph = []
n = int(input())
for i in range(0,n):
    RGBGraph.append(list(input()))
RBGraph = [['R' if value == 'G' else value for value in row] for row in RGBGraph]
visitedRGB = [[False for _ in range(n)] for _ in range(n)]
visitedRB = [[False for _ in range(n)] for _ in range(n)]
def find_area(x, y, graph, visited):
    def dfs(x, y, RGB):
        if x < 0 or x >= n or y < 0 or y >= n:
            return False
        if visited[x][y] == False and graph[x][y] == RGB:
            visited[x][y] = True
            dfs(x - 1, y,RGB)
            dfs(x, y - 1,RGB)
            dfs(x + 1, y,RGB)
            dfs(x, y + 1,RGB)
            return True
        return False
    red = dfs(x,y,'R')
    green = dfs(x,y,'G')
    blue = dfs(x,y,'B')
    return red+green+blue

# find RGB
resultRGBArea = 0
for i in range(n):
    for j in range(n):
        resultRGBArea += find_area(i, j, RGBGraph,visitedRGB)
resultRBArea = 0
for i in range(n):
    for j in range(n):
        resultRBArea += find_area(i, j, RBGraph,visitedRB)
print(resultRGBArea, resultRBArea)