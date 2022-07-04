N = int(input())
arr = list(set([input() for _ in range(N)]))
arr.sort(key=lambda x: (len(x), x))
for elem in arr:
    print(elem)