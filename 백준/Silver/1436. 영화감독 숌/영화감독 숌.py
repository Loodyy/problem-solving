cnt, now = 0, 0
n = int(input())
while cnt < n:
    now += 1
    if "666" in str(now):
        cnt += 1
    
print(now)