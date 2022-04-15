def solve():
    result = 0

    temp = [0]
    tmp = 0
    for p in prime:
        tmp += p
        temp.append(tmp)

    start, end = 1, 1
    length = len(temp)
    while start <= end and start < length and end < length:
        sum = temp[end] - temp[start-1]
        if sum >= n:
            start += 1
        else:
            end += 1
        if sum == n:
            result += 1

    print(result)
    return

if __name__ == "__main__":

    n = int(input())
    arr = [True for _ in range(n+1)]
    
    for i in range(2, int(n**(1/2))+1):
        if arr[i]:
            mul = 2
            while i*mul <= n:
                arr[i*mul] = False
                mul += 1

    prime = []
    for i in range(2, n+1):
        if arr[i]: prime.append(i)

    solve()