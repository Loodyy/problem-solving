from collections import deque

def solve():
    day = 0

    while True:
        change = False
        visited = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                pnum = 0
                num = 0
                if not visited[i][j]:
                    pnum += arr[i][j]
                    num += 1
                    union = []
                    q = deque([[j, i]])
                    visited[i][j] = True
                    union.append((j, i))
                    while q:
                        x, y = q.popleft()
                        for d in dir:
                            dx, dy = d[0], d[1]
                            if 0 <= x+dx < n and 0 <= y+dy < n and not visited[y+dy][x+dx]:
                                if l <= abs(arr[y][x]-arr[y+dy][x+dx]) <= r:    
                                    visited[y+dy][x+dx] = True
                                    union.append((x+dx, y+dy))
                                    q.append((x+dx, y+dy))
                                    pnum += arr[y+dy][x+dx]
                                    num += 1
                else:
                    continue
                if num > 1:
                    change = True
                    avg = int(pnum / num)
                    for u in union:
                        arr[u[1]][u[0]] = avg
                
        if not change:
            print(day)
            return 
        day += 1

if __name__ == "__main__":

    n, l, r = map(int, input().split()) # nxn, l <= p diff <= r
    arr = [list(map(int, input().split())) for _ in range(n)]

    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    solve()