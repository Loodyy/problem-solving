n = int(input())
tar = 0
for i in range(1, n+1):
    if n == i + sum([int(x) for x in str(i)]):
        tar = i 
        break

print(tar)