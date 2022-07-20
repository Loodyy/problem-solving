n = int(input())
now = 1
for _ in range(n):
    a, b = map(int, input().split())
    if now == a: now = b
    elif now == b: now = a
print(now)