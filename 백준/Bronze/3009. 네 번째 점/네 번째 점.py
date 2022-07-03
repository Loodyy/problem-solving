xs, ys = set(), set()
for i in range(3):
    a, b = map(int, input().split())
    if a in xs: xs.remove(a)
    else: xs.add(a)
    if b in ys: ys.remove(b)
    else: ys.add(b)

print(xs.pop(), ys.pop())