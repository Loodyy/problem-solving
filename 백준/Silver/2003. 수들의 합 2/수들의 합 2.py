N, M = map(int, input().split())
arr = list(map(int, input().split()))

sums = [0] * N
for i in range(N):
    sums[i] = sums[i-1] + arr[i]
sums.append(0) # dummy

cnt = 0
s, e = 0, 0
while s <= e and e < N:
    sum = sums[e] - sums[s-1]
    if sum <= M:
        if sum == M:
            cnt += 1
        e += 1
    else:
        if s == e:
            e += 1
        s += 1

print(cnt)