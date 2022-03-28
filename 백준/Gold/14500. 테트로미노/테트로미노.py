n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

max_value = max(map(max, arr))

result = 0

def dfs(x, y, cnt, sum):
    global result 
    
    if result >= sum + (3-cnt) * max_value:
        return

    if cnt == 3:
        result = max(result, sum)
        return

    for d in dir:
        dx = x + d[0]
        dy = y + d[1]
        if 0 <= dx < m and 0 <= dy < n and visited[dy][dx] == False:
            if cnt == 1:
                visited[dy][dx] = True
                dfs(x, y, cnt+1, sum + arr[dy][dx])
                visited[dy][dx] = False
            visited[dy][dx] = True
            dfs(dx, dy, cnt+1, sum + arr[dy][dx])
            visited[dy][dx] = False
        

def solve():
    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            dfs(j, i, 0, arr[i][j])
            visited[i][j] = False
    
    print(result)

solve()