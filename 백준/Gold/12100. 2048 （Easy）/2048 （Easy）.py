import copy

def left(arr):
    for i in range(n):
        target = 0
        for j in range(1, n):
            if arr[i][j]:
                temp, arr[i][j] = arr[i][j], 0
                if arr[i][target] == 0:
                    arr[i][target] = temp
                elif arr[i][target] == temp:
                    arr[i][target] *= 2
                    target += 1
                else:
                    target += 1
                    arr[i][target] = temp
    return arr

def right(arr):
    for i in range(n):
        target = n-1
        for j in range(n-2, -1, -1):
            if arr[i][j]:
                temp, arr[i][j] = arr[i][j], 0
                if arr[i][target] == 0:
                    arr[i][target] = temp
                elif arr[i][target] == temp:
                    arr[i][target] *= 2
                    target -= 1
                else:
                    target -= 1
                    arr[i][target] = temp
    return arr
    
def up(arr):
    for j in range(n):
        target = 0
        for i in range(1, n):
            if arr[i][j]:
                temp, arr[i][j] = arr[i][j], 0
                if arr[target][j] == 0:
                    arr[target][j] = temp
                elif arr[target][j] == temp:
                    arr[target][j] *= 2
                    target += 1
                else:
                    target += 1
                    arr[target][j] = temp
    return arr

def down(arr):
    for j in range(n):
        target = n-1
        for i in range(n-2, -1, -1):
            if arr[i][j]:
                temp, arr[i][j] = arr[i][j], 0
                if arr[target][j] == 0:
                    arr[target][j] = temp
                elif arr[target][j] == temp:
                    arr[target][j] *= 2
                    target -= 1
                else:
                    target -= 1
                    arr[target][j] = temp
    return arr

def dfs(arr, cnt):
    if cnt == 5:
        temp = []
        for i in arr:
            temp.append(max(i))
        return max(temp)

    a = dfs(left(copy.deepcopy(arr)), cnt + 1)
    b = dfs(right(copy.deepcopy(arr)), cnt + 1)
    c = dfs(up(copy.deepcopy(arr)), cnt + 1)
    d = dfs(down(copy.deepcopy(arr)), cnt + 1)
    return max(a, b, c, d)


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

print(dfs(arr, 0))