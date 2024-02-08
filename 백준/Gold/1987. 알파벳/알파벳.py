# R. C
import copy

row, cal = map(int, input().split())
board = []
stack = set([])
for i in range(row):
    board.append(list(input()))
def search_best_way(x, y):
    if x < 0 or x >= row or y < 0 or y >= cal:
        return 0
    if (board[x][y] in stack) == False:
        stack.add(board[x][y])
        maxWay = -1
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)] :
            value = search_best_way(x + dx, y + dy)
            maxWay = max(maxWay,value)
        stack.remove(board[x][y])
        return maxWay+1
    return 0

print(search_best_way(0,0))
