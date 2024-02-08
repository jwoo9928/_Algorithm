def solution(n, computers):
    visited = [False] * n  
    answer = 0

    def dfs(computer):
        visited[computer] = True  
        for i in range(n): 
            if computers[computer][i] == 1 and not visited[i]:
                dfs(i)

    for i in range(n):  
        if not visited[i]:  
            dfs(i)  
            answer += 1  

    return answer