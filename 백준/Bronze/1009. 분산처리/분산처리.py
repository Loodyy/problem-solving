k = int(input())

for _ in range(k):
    a, b = map(int, input().split())
    now = a%10
    loop = [now]
    for i in range(1, b+1): 
        now = (now*a)%10
        if now == a:
            break
        loop.append(now)

    
    idx = b % len(loop)
    res = loop[idx-1]
    if res == 0:
        res = 10
    print(res)