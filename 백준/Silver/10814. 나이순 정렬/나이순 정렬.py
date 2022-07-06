import sys
input = sys.stdin.readline

k = int(input())
arr = []
for idx in range(k):
    age, name = input().split()
    arr.append((int(age), name, idx))

arr.sort(key=lambda x: (x[0], x[2]))

for i in range(k):
    print(*arr[i][:2])