N, M = map(int, input().split())
arr = list(map(int, input().split()))

sums = [0] * N
for i in range(N):
    sums[i] = sums[i-1] + arr[i]
sums.append(0) # dummy

cnt = 0
for i in range(N):
    for j in range(i, N):
        if sums[j] - sums[i-1] == M:
            cnt += 1

print(cnt)