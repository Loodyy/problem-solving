from collections import deque

def solve(n, arr):
    answer = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "0" or visited[i][j]:
                continue
            cnt = bfs(j, i, arr, visited)        
            answer.append(cnt)
    
    answer.sort()
    print(len(answer))
    for ans in answer:
        print(ans)
    return

def bfs(x, y, arr, visited):
    res = 1
    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    q = deque([(x, y)])
    visited[y][x] = True
    while q:
        x, y = q.popleft()
        for d in dir:
            tx, ty = x+d[0], y+d[1]
            if is_valid_pos(tx, ty, arr, visited):
                visited[ty][tx] = True
                q.append((tx, ty))
                res += 1

    return res

def is_valid_pos(x, y, arr, visited):
    return 0 <= x < n and 0 <= y < n \
        and visited[y][x] == False and arr[y][x] == "1"


n = int(input())
arr = [list(input()) for _ in range(n)]
solve(n, arr)
