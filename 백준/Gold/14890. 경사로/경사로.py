def solve(arr):
    global result 

    for i in range(n):
        visited = [False]*n
        left, right = False, False
        now = arr[i][0]
        for j in range(n):
            if left:
                break
            diff = arr[i][j] - now
            if diff == 0:
                continue
            elif diff == 1:
                for k in range(l):
                    if 0 <= j-1-k < n and arr[i][j-1-k] == arr[i][j-1] and visited[j-1-k] == False:
                        visited[j-1-k] = True
                    else:
                        left = True 
                        break

            elif diff == -1:
                for k in range(l):
                    if 0 <= j+k < n and  arr[i][j+k] == arr[i][j] and visited[j+k] == False:
                        visited[j+k] = True
                    else: 
                        left = True
                        break
            else:
                left = True 
                break 
            now = arr[i][j]
        
        if left:
            visited = [False]*n
            now = arr[i][n-1]
            for j in range(n):
                if right:
                    break
                diff = arr[i][n-1-j] - now
                if diff == 0:
                    continue
                elif diff == 1:
                    for k in range(l):
                        if 0 <= n-j+k < n and arr[i][n-j+k] == arr[i][n-j] and visited[n-j+k] == False:
                            visited[n-j+k] = True
                        else:
                            right = True 
                            break
                elif diff == -1:
                    for k in range(l):
                        if 0 <= n-1-j-k < n and arr[i][n-1-j-k] == arr[n-1-j] and visited[n-1-j-k] == False:
                            visited[n-1-j-k] = True
                        else:
                            right = True
                            break
                else: 
                    right = True
                    break
                now = arr[i][n-1-j]

        if left and right:
            continue
        else:
            result += 1

def rotate():
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = arr[j][n-i-1]
    return temp

if __name__ == "__main__":
    n, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    solve(arr)
    a = rotate()
    solve(a)
    print(result)
