def solve(arr):

    leng = [len(x) for x in arr]
    dp = [[[0] * (leng[0]+1) for __ in range(leng[1]+1)] for ___ in range(leng[2]+1)]

    maxV = 0
    for i in range(1, leng[2]+1):
        for j in range(1, leng[1]+1):
            for k in range(1, leng[0]+1):
                if arr[0][k-1] == arr[1][j-1] and arr[0][k-1] == arr[2][i-1]: 
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else: 
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
                maxV = max(maxV, dp[i][j][k])
    return maxV

def main():

    arr = [input() for _ in range(3)]
    print(solve(arr))

if __name__ == "__main__":

    main()
