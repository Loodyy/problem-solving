k = int(input())

for _ in range(k):
    res = ""
    n, s = input().split()
    n = int(n)
    for x in s:
        res += x*n
    print(res)