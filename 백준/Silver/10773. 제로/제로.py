import sys
input = sys.stdin.readline

K = int(input())

arr = []
for i in range(K):
    num = int(input())
    if num != 0:
        arr.append(num)
    else:
        arr.pop()

print(sum(arr))