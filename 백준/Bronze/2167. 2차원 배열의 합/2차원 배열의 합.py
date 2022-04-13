import sys
input = sys.stdin.readline

def solve():

    for sum in sums:
        i, j, x, y = sum
        temp = 0
        if i == x and j == y:
            temp = arr[i-1][j-1]
        elif i == x:
            for a in range(j, y+1): temp += arr[i-1][a-1]
        elif j == y:
            for b in range(i, x+1): temp += arr[b-1][j-1]
        else:
            for a in range(i, x+1):
                for b in range(j, y+1):
                    temp += arr[a-1][b-1]

        print(temp)

    return



if __name__ == "__main__":

    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = int(input())
    sums = [list(map(int, input().split())) for _ in range(cnt)]

    solve()