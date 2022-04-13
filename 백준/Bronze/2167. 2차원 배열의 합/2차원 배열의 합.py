import sys
input = sys.stdin.readline

def solve():

    prefix = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            prefix[i][j] = arr[i-1][j-1] + prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1]

    for sum in sums:
        i, j, x, y = sum
        temp = prefix[x][y] - prefix[i-1][y] - prefix[x][j-1] + prefix[i-1][j-1]
        print(temp)

    return

if __name__ == "__main__":

    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = int(input())
    sums = [list(map(int, input().split())) for _ in range(cnt)]

    solve()