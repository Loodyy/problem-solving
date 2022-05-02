from collections import deque

def solve():

    cnt = 1
    while True:
        for _ in range(len(q)):
            x, y = q.popleft()
            for d in dir:
                dx, dy = x+d[0], y+d[1]
                if 0 <= dx < m and 0 <= dy < n:
                    if not visited_w[dy][dx] and arr[dy][dx] != "X" and (dx, dy) != dst:
                        visited_w[dy][dx] = True
                        arr[dy][dx] = "*"
                        q.append((dx, dy))
        
        for _ in range(len(b)):
            sx, sy = b.popleft()
            for d in dir:
                dx, dy = sx+d[0], sy+d[1]
                if 0 <= dx < m and 0 <= dy < n:
                    if (dx, dy) == dst:
                        print(cnt)
                        return
                    if arr[dy][dx] != "*" and arr[dy][dx] != "X":
                        if not visited_b[dy][dx]:
                            visited_b[dy][dx] = True
                            b.append((dx, dy))
        
        for i in range(n):
            for j in range(m):
                if visited_b[i][j] and visited_w[i][j]:
                    visited_b[i][j] = False
        
        check = 0
        for x in visited_b:
            check += x.count(True)
        if not check:
            print("KAKTUS")
            return
        cnt += 1

if __name__ == "__main__":

    n, m = map(int, input().split())
    arr = []
    visited_w = [[False] * m for _ in range(n)]
    visited_b = [[False] * m for _ in range(n)]
    q, b = deque(), deque()
    dst = 0
    for i in range(n):
        temp = list(input())
        for j, x in enumerate(temp):
            if x == "D": dst = (j, i)
            elif x == "S": 
                visited_b[i][j] = True
                b.append((j, i))
            elif x == "*":
                visited_w[i][j] = True 
                q.append((j, i))
        arr.append(temp)
    
    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    solve()
