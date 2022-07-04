n, m = map(int, input().split())
prime = [True] * (m+1)
prime[0], prime[1] = False, False

for i in range(2, int(m**0.5)+1):
    if prime[i]:
        for j in range(i*i, m+1, i):
            prime[j] = False

for i in range(n, m+1):
    if prime[i]:
        print(i)
