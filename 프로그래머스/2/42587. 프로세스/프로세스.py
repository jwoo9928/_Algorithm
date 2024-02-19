from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = deque((i, priorities[i]) for i in range(len(priorities)))
    count = 0
    while priorities:
        index, process = priorities.popleft()
        if len(priorities) <= 0:
            return count+1
        if max(priorities, key=lambda x: x[1])[1] > process:
            priorities.append((index, process))
        else:
            count+=1
            if index == location:
                return count
    return count