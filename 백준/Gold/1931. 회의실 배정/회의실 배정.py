n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))
end = 0
cnt = 0
for i in range(n):
    if meetings[i][0] >= end:
        end = meetings[i][1]
        cnt += 1
print(cnt)