from collections import deque

def solve():
    result = 0

    for idx, d, u in query:
        move = u if d == 0 else -u
        for i in range(1, n+1):
            if not i%idx:
                arr[i-1].rotate(move)
        remain()

    for i, x in enumerate(arr):
         for j, y in enumerate(x):
             result += arr[i][j]

    print(result)
    return

def remain():
    total = 0
    num = 0
    avg_check = False
    visited = [[False] * m for _ in range(n)]
    for i, x in enumerate(arr):
         for j, y in enumerate(x):
             total += y
             if y: # remain
                target = y
                num += 1
                check = False
                for d in dir:
                    x, y = (j+d[0])%m, i+d[1]
                    if 0 <= y < n and arr[y][x] == target:
                        visited[y][x] = True
                        check = True
                if check:
                    visited[i][j] = True
                    avg_check = True 

    for i in range(n):
        for j in range(m):
            if visited[i][j]: arr[i][j] = 0

    if not avg_check and num:
        avg = total/num
        for i, x in enumerate(arr):
            for j, y in enumerate(x):
                if y > avg: arr[i][j] -= 1
                elif y != 0 and y < avg: arr[i][j] += 1
    return

if __name__ == "__main__":

    n, m, t = map(int, input().split())

    arr = [deque() for _ in range(n)]
    for i in range(n):
        arr[i].extend(list(map(int, input().split())))
    query = [list(map(int, input().split())) for _ in range(t)]

    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    solve()
