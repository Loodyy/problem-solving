def solve(arr):

    page = [[0] * (101) for _ in range(101)]
    result = []

    for x, y in arr:
        for i in range(y, y+10):
            for j in range(x, x+10):
                page[i][j] = 1

    for i in range(1, 100):
        for j in range(100):
            if page[i][j] == 1:
                page[i][j] += page[i-1][j]

    for i in range(1, 100):
        for j in range(100):
            h = 100
            for k in range(j, 100):
                h = min(h, page[i][k])
                if h == 0: break

                area = h*(k-j+1)
                result.append(area)

    print(max(result))
    return

if __name__ == "__main__":

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    solve(arr)
