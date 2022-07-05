import sys
input = sys.stdin.readline

from collections import Counter

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
temp = sorted(Counter(arr).most_common(), key=lambda x: (-x[1], x[0]))
res = temp[0][0]
if len(temp) > 1:
    if temp[1][1] == temp[0][1]:
        res = temp[1][0]

print(round(sum(arr)/n))
print(arr[n//2])
print(res)
print(arr[-1]-arr[0])