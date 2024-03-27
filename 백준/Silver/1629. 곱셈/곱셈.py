def power(a, n):
    if n == 0:
        return 1
    sub = power(a, n // 2)    
    if n % 2 == 0:
        return (sub**2) % c
    else:
        return (a * sub**2) % c

a, b, c = map(int, input().split())
print(power(a, b) % c)