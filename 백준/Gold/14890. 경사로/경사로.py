def solve(arr):
    global result 

    bool_arr = check(arr)
    for i in bool_arr:
        if not i: result += 1

    temp = rotate()
    bool_arr = check(temp)
    for i in bool_arr:
        if not i: result += 1

# 90도 회전
def rotate():
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = arr[j][n-i-1]
    return temp

# 각 줄마다 좌에서 오른쪽으로만 길이 완성되는지 체크
def check(arr):
    global result
    bool_arr = []
    for i in range(n):
        visited = [False]*n
        bool = False
        now = arr[i][0]
        for j in range(n):
            if bool:
                break
            diff = arr[i][j] - now
            if diff == 0:
                continue
            elif diff == 1:
                for k in range(l):
                    if 0 <= j-1-k < n and arr[i][j-1-k] == arr[i][j-1] and visited[j-1-k] == False:
                        visited[j-1-k] = True
                    else:
                        bool = True
                        break
            elif diff == -1:
                for k in range(l):
                    if 0 <= j+k < n and  arr[i][j+k] == arr[i][j] and visited[j+k] == False:
                        visited[j+k] = True
                    else: 
                        bool = True
                        break
            else:
                bool = True 
                break 
            now = arr[i][j]
        bool_arr.append(bool)

    return bool_arr

if __name__ == "__main__":
    n, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    solve(arr)
    print(result)