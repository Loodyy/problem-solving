MAX = int(1e7)

def solve():
    result = 0

    temp = [0]
    tmp = 0
    for p in prime:
        tmp += p
        temp.append(tmp)

    start, end = 1, 1
    while start <= end:
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

    arr = [True for _ in range(MAX+1)]
    n = int(input())

    for i in range(2, int(MAX**(1/2))+1):
        if arr[i]:
            mul = 2
            while i*mul <= MAX:
                arr[i*mul] = False
                mul += 1

    prime = []
    for i in range(2, MAX+1):
        if arr[i]: prime.append(i)

    solve()