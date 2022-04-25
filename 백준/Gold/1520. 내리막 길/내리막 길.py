import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def solve(x, y):
    if x == m-1 and y == n-1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]
        
    dp[y][x] = 0

    for d in dir:
        tx, ty = x+d[0], y+d[1]
        if 0 <= tx < m and 0 <= ty < n:
            if arr[y][x] > arr[ty][tx]:
                dp[y][x] += solve(tx, ty)
                
    return dp[y][x]

if __name__ == "__main__":

    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)] # 0, 0 -> n-1, n-1

    dp = [[-1] * m for _ in range(n)]
    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    print(solve(0, 0))
