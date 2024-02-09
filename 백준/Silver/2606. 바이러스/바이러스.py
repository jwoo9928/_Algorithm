from collections import deque
n = int(input())
k = int(input())
computers = [-1 for _ in range(n+1)]
graph = []
queue = deque([])
for g in range(k):
    graph.append(list(map(int, input().split(" "))))

def search_infected():
    queue.append(1)
    while queue:
        v = queue.popleft()
        computers[v-1] = 0
        for c_pairs in graph:
            if v in c_pairs:
                for c in c_pairs:
                    if computers[c-1] < 0:
                        queue.append(c)

search_infected()
print(computers.count(0)-1)
