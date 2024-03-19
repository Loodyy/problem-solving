n, s = map(int, input().split())
arr = list(map(int, input().split()))

sums = arr[::]
for i in range(1, n):
    sums[i] = sums[i - 1] + arr[i]
sums.append(0)

srt, end = -1, 0
min_num_len = n + 1
while srt < end and end < n:
    sum = sums[end] - sums[srt]
    if sum >= s:
        min_num_len = min(min_num_len, end - srt)
        srt += 1
    else:
        end += 1

print(min_num_len if min_num_len < n + 1 else 0)