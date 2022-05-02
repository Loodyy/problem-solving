from collections import deque

def solve():

    while q:
        x, y = q.popleft()
        if arr[dst_y][dst_x] == "S": 
            print(visited[dst_y][dst_x])
            return
        for d in dir:
            tx, ty = x+d[0], y+d[1]
            if 0 <= tx < m and 0 <= ty < n:
                temp = arr[ty][tx]
                if arr[y][x] == "S" and (temp == "." or temp == "D"):
                    arr[ty][tx] = "S"
                    visited[ty][tx] = visited[y][x] + 1
                    q.append((tx, ty))
                elif arr[y][x] == "*" and (temp == "." or temp == "S"):
                    arr[ty][tx] = "*"
                    q.append((tx, ty))
    print("KAKTUS")
    return

if __name__ == "__main__":

    n, m = map(int, input().split())
    arr = []
    visited = [[0] * m for _ in range(n)]
    q = deque()
    dst_x, dst_y = 0, 0
    for i in range(n):
        temp = list(input())
        for j, x in enumerate(temp):
            if x == "D": dst_x = j; dst_y = i
            elif x == "S": q.append((j, i))
        arr.append(temp)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "*": q.append((j, i))

    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    solve()
