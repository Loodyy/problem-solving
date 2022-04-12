import heapq
INF = int(1e3)

def solve():
    result = 0

    q = []
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0
    
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[y][x] < dist:
            continue
        for d in dir:
            dx, dy = d[0], d[1]
            if 0 <= x+dx < m and 0 <= y+dy < n:
                cost = dist + arr[y+dy][x+dx]
                if cost < distance[y+dy][x+dx]:
                    distance[y+dy][x+dx] = cost
                    heapq.heappush(q, (cost, x+dx, y+dy))

    result = distance[n-1][m-1]

    print(result)
    return

if __name__ == "__main__":

    m, n = map(int, input().split())
    arr = [list(map(int, str(input()))) for _ in range(n)]

    distance = [[INF]*m for _ in range(n)] 
    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    solve()
