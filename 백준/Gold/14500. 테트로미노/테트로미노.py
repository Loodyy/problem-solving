n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

def a():
    result = []
    for i in range(n-1):
        for j in range(m-1):
            result.append(arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1])
    return max(result)

def b():
    result = []
    for i in range(n):
        for j in range(m-3):
            result.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i][j+3])
    for i in range(n-3):
        for j in range(m):
            result.append(arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+3][j])
    return max(result) 

def c(): 
    result = []
    for i in range(n-2):
        for j in range(m-1):
            result.append(arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j+1])
            result.append(arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j+1])
            result.append(arr[i+2][j] + arr[i+2][j+1] + arr[i+1][j+1] + arr[i][j+1])
            result.append(arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+2][j])
    for i in range(n-1):
        for j in range(m-2):
            result.append(arr[i][j+2] + arr[i+1][j+2] + arr[i+1][j+1] + arr[i+1][j])
            result.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+2])
            result.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j])
            result.append(arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2])
    return max(result)

def d(): 
    result = []
    for i in range(n-2):
        for j in range(m-1):
            result.append(arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1])
            result.append(arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j])
    for i in range(n-1):
        for j in range(m-2):
            result.append(arr[i+1][j] + arr[i+1][j+1] + arr[i][j+1] + arr[i][j+2])
            result.append(arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j+2])
    return max(result)

def e():
    result = []
    for i in range(n-1):
        for j in range(m-2):
            result.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1])
            result.append(arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2])
    for i in range(n-2):
        for j in range(m-1):
            result.append(arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+1][j+1])
            result.append(arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j] + arr[i+2][j+1])
    return max(result)

def solve():
    i = a()
    j = b()
    k = c()
    m = d()
    n = e()

    print(max(i, j, k, m, n))

solve()