from bisect import bisect_left, bisect_right

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

def get_sums(arr):
    l = len(arr)
    ret = []
    for i in range(1, l+1):
        temp = sum(arr[:i])
        ret.append(temp)
        for j in range(l-i):
            temp = temp - arr[j] + arr[i+j]
            ret.append(temp)
    return sorted(ret)
a_sums = get_sums(A)
b_sums = get_sums(B)

if len(a_sums) > len(b_sums):
    a_sums, b_sums = b_sums, a_sums

ans = 0
for a_sum in a_sums:
    target = T - a_sum
    li, ri = bisect_left(b_sums, target), bisect_right(b_sums, target)
    ans += ri - li

print(ans)