import sys
input = sys.stdin.readline

def solve(n, t, arr):
    result = 0

    candy = []
    for cal, price in arr:
        cal, price = int(cal), round(float(price)*100)
        candy.append([price, cal])
    candy.sort()

    dp = [0] * (t+1)
    for i in range(t+1): # 10000
        if i == 200:
            a=1
        for price, cal in candy:
            if i-price >= 0: # 5000
                dp[i] = max(dp[i], dp[i-price]+cal)
            else:
                break

    result = max(dp)
    return result

def main():

    while True:
        n, t = input().split()
        n, t = int(n), round(float(t)*100)
        if n == 0 and t == 0:
            return
        arr = [list(input().split()) for _ in range(n)]
        print(solve(n, t, arr))

if __name__ == "__main__":

    main()
