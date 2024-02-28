def solution(triangle):
    dp = [[0 for _ in range(len(tri))] for tri in triangle]
    dp[0][0] = triangle[0][0]
    for i in range(0, len(triangle)-1):
        tri = triangle[i]
        for j in range(len(tri)):
            stand = dp[i][j]
            dp[i+1][j] = max(stand + triangle[i+1][j], dp[i+1][j])
            dp[i+1][j+1] = max(stand + triangle[i+1][j+1],dp[i+1][j+1])
    return max(dp[len(triangle)-1])