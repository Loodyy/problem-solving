from collections import deque
from itertools import combinations as cb
from copy import deepcopy as dc
INF = int(1e5)

def solve():
    
    res = []

    comb = list(cb(candi, m))
    for com in comb:
        res.append(bfs(arr, com))

    result = min(res) if min(res) != INF else -1
    print(result)
    return

def bfs(temp, birus):

    arr = dc(temp)

    q = deque()
    for x, y in birus:
        q.append((x, y))
        arr[y][x] = 0
    
    while q:
        x, y = q.popleft()
        for d in dir:
            tx, ty = x+d[0], y+d[1]
            if 0 <= tx < n and 0 <= ty < n:
                if arr[ty][tx] == 0 and (tx, ty) not in birus:
                    arr[ty][tx] = arr[y][x] + 1
                    q.append((tx, ty))
    
    check = True
    max_v = 0
    for x, y in candi:
        arr[y][x] = -1

    for i, x in enumerate(arr):
        if not check:
            break
        for j, y in enumerate(x):
            if arr[i][j] == 0:
                check = False
                break
            max_v = max(max_v, y)
    
    return max_v if check else INF

if __name__ == "__main__":

    n, m = map(int, input().split())
    arr = []
    candi = []
    for i in range(n):
        temp = list(map(int, input().split()))
        for j, x in enumerate(temp):
            if x == 1:
                temp[j] = -1 # wall
            elif x == 2:
                temp[j] = 0 # birus
                candi.append((j, i)) # x, y
        arr.append(temp)

    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    solve()
