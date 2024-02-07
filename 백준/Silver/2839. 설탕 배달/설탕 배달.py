import sys

sys.setrecursionlimit(10000)
N = int(input())
memo = [-1 for _ in range(N+1)]

def rec_minus(N):
    if N == 0:
        return 0
    if N - 5 >= 0:
        result = memo[N-5] if memo[N-5] != -1 else rec_minus(N-5)
        if result != -1 :
            memo[N-5] = result+1
            return memo[N-5]
    if N - 3 >= 0:
        result = memo[N - 3] if memo[N - 3] != -1 else rec_minus(N - 3)
        if result != -1 :
            memo[N - 3] = result + 1
            return memo[N - 3]
    return -1


print(rec_minus(N))