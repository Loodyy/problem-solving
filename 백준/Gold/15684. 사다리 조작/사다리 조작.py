def check():
    for i in range(n):
        now = i
        for j in range(h):
            if point[j][now]:
                now += 1
            elif now > 0 and point[j][now-1]:
                now -= 1
        if now != i:
            return False

    return True

def dfs(x, y, cnt):
    global result

    if check():
        result = min(result, cnt)
        return
    elif cnt == 3 or result <= cnt:
        return

    for i in range(y, h):
        if i != y: x = 0
        for j in range(x, n-1):
            if not point[i][j] and not point[i][j+1]:
                point[i][j] += 1
                dfs(j+2, i, cnt+1)
                point[i][j] -= 1
     

if __name__ == "__main__":
    n, m, h = map(int, input().split())
    point = [[0]*n for _ in range(h)]
    for _ in range(m):
        y, x = map(int, input().split())
        point[y-1][x-1] = 1

    result = 4

    dfs(0, 0, 0)

    if result < 4:
        print(result)
    else: print(-1)

