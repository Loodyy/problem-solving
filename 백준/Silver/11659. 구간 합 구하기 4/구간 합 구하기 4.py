def solve():
    
    prefix_sum = [arr[0]]
    for i in range(1, len(arr)):
        prefix_sum.append(arr[i] + prefix_sum[i-1])

    for sum in sums:
        start, end = sum[0]-2, sum[1]-1
        if start != -1:
            print(prefix_sum[end] - prefix_sum[start])
        else: print(prefix_sum[end])

    return

if __name__ == "__main__":

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    sums = [list(map(int, input().split())) for _ in range(m)]

    solve()