n = int(input()) # n <= 100
arr = []
for _ in range(n):
    a, b = map(int, input().split()) # a, b <= 500
    arr.append((a, b))

arr.sort()
arrb = []
for x in arr:
    arrb.append(x[1])

lis = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if arrb[i] > arrb[j]:
            lis[i] = max(lis[i], lis[j] + 1)

print(n - max(lis))
    