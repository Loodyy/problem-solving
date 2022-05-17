def solve(n):

    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            temp = 0
            if prime(int(str(i)+str(j))):
                temp = 1
            dp[i][j] = max(dp[i-1][j]+temp, dp[i][j-1]+temp)
            if i == n and j == n:
                print(dp[i][j]-1)
                return

def prime(x):
    if not x or x == 1: return False
    else:
        if x == 2: return True
        for i in range(2, int(x**(1/2)+1)):
            if not x%i: return False
        return True

if __name__ == "__main__":

    n = int(input())

    solve(n) 