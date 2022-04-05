def cv(x, y, direction, temp):
    for d in direction:
        tx, ty = x, y
        while True:
            tx, ty = tx+dir[d][0], ty+dir[d][1]
            if 0 <= tx < m and 0 <= ty < n and temp[ty][tx] != 6:
                if temp[ty][tx] == 0:
                    temp[ty][tx] = -1
            else:
                break
            

def solve(arr, cnt):
    global result
 
    temp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = arr[i][j]

    if cnt == len(obj):
        tmp = 0
        for i in temp:
            for j in i:
                if j == 0:
                    tmp += 1
        result.append(tmp)
        return

    x, y, idx = obj[cnt]

    for d in directions[idx-1]:
        cv(x, y, d, temp)
        solve(temp, cnt+1)
        for i in range(n):
            for j in range(m):
                temp[i][j] = arr[i][j] # solve 돌기 전 arr로 되돌리기

    return

if __name__ == "__main__":
    obj = []
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(m):
            if 0 < temp[j] < 6:
                obj.append((j, i, temp[j])) # x, y, idx
        arr.append(temp)

    directions = [
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [3, 0]],
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
        [[0, 1, 2, 3]]
    ]

    dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    result = []

    solve(arr, 0)
    print(min(result))
 
