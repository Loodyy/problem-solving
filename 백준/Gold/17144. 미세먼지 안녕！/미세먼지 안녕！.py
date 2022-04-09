from collections import deque
from copy import deepcopy as dc

def solve(t):
    cnt = 0

    while True:
        if cnt == t:
            print(sum(map(sum, arr))+2)
            return

        # 미세먼지
        arr_temp = [[0 for _ in range(m)] for _ in range(n)] 
        while q:
            x, y = q.pop()
            dcnt = 0
            di = []
            for d in dir:
                tx, ty = x+d[0], y+d[1]
                if [tx, ty] not in air and 0 <= tx < m and 0 <= ty < n:                    
                    dcnt += 1
                    di.append(d)
            plus = arr[y][x] // 5
            arr_temp[y][x] -= plus * dcnt
            for d in di:
                tx, ty = x+d[0], y+d[1]
                arr_temp[ty][tx] += plus
        
        for i in range(n):
            for j in range(m):
                arr[i][j] += arr_temp[i][j] 
        # 확산

        # cleaner
        # upper side
        for i in range(air[0][1], 0, -1):
            x, y = 0, i
            if arr[y][x] != -1:
                arr[y][x] = arr[y-1][x]
        
        for i in range(1, m):
            x, y = i, 0
            arr[y][x-1] = arr[y][x]
        
        for i in range(air[0][1]):
            x, y = m-1, i
            arr[y][x] = arr[y+1][x]
        
        for i in range(m-1, 1, -1):
            x, y = i, air[0][1]
            arr[y][x] = arr[y][x-1]
            if x == 2:
                arr[y][x-1] = 0
        # lower side
        for i in range(air[1][1], n-1):
            x, y = 0, i
            if arr[y][x] != -1:
                arr[y][x] = arr[y+1][x]

        for i in range(m-1):
            x, y = i, n-1
            arr[y][x] = arr[y][x+1]
        
        for i in range(n-1, air[1][1], -1):
            x, y = m-1, i
            arr[y][x] = arr[y-1][x]

        for i in range(m-1, 1, -1):
            x, y = i, air[1][1]
            arr[y][x] = arr[y][x-1]
            if x-1 == 1:
                arr[y][x-1] = 0

        # next stage deque
        for i in range(n):
            for j in range(m):
                if arr[i][j] > 0:
                    q.append([j, i])

        cnt += 1

if __name__ == "__main__":
    n, m, t = map(int, input().split())
    arr = []
    air = []
    q = deque()
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(m):
            if temp[j] == -1:
                air.append([j, i])
            elif temp[j] > 0:
                q.append([j, i])
        arr.append(temp)

    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    solve(t)