def solve(n, max_v):
    prime_c = prime(max_v)
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            temp = 0
            if prime_c[int(str(i)+str(j))]:
                temp = 1
            dp[i][j] = max(dp[i-1][j]+temp, dp[i][j-1]+temp)
            if i == n and j == n:
                print(dp[i][j]-1)
                return

def prime(max_v):

    prime_c = [True] * (max_v+1)
    for i in range(2): prime_c[i] = False
    for i in range(2, max_v+1):
        mul = 2
        while i*mul <= max_v: 
            if prime_c[i*mul]:
                prime_c[i*mul] = False
            mul += 1

    return prime_c

if __name__ == "__main__":

    n = int(input())
    max_v = int(str(n)+str(n))
    solve(n, max_v) 