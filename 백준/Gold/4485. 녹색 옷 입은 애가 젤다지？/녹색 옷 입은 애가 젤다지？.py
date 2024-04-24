import sys, heapq
input = sys.stdin.readline

T = 1
while True:
    N = int(input())
    if N == 0:
        break

    def in_range(x, y):
        return 0 <= x < N and 0 <= y < N

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float("inf")] * N for _ in range(N)]
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    q = []
    heapq.heappush(q, (arr[0][0], 0, 0))
    while q:
        cost, x, y = heapq.heappop(q)
        if x == N-1 and y == N-1:
            print(f"Problem {T}: {visited[N-1][N-1]}")
            break
        if visited[x][y] < cost:
            continue
        for tx, ty in dirs:
            nx, ny = x+tx, y+ty
            if not in_range(nx, ny):
                continue
            ncost = cost + arr[nx][ny]
            if ncost < visited[nx][ny]:
                visited[nx][ny] = ncost
                heapq.heappush(q, (ncost, nx, ny))
    T += 1