n, k = int(input()), int(input())
n -= n%100
for i in range(100):
    if (n+i)%k == 0:
        print(str(i).zfill(2))
        break