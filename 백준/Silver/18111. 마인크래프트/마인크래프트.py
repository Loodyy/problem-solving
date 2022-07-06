n, m, b = map(int, input().split())
arr = []
for _ in range(n):
    arr.extend(list(map(int, input().split())))

T, H = int(1e9), -1
for h in range(257):
    cut, fill = 0, 0
    for elem in arr:
        if elem >= h:
            cut += elem - h
        else:
            fill += h - elem
    t = cut*2 + fill
    
    if b+cut-fill >= 0 and T >= t:
        T, H = t, h

print(T, H)