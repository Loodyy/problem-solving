n = int(input())
arr = set(map(int, input().split()))

m = int(input())
temp = list(map(int, input().split()))
for elem in temp:
    if elem in arr:
        print(1)
    else:
        print(0)
