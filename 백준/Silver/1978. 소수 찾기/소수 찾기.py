prime = [True] * (1001)
prime[0] = prime[1] = False
for i in range(2, int(1001**0.5)+1):
    if prime[i]:
        for j in range(i*i, 1001, i):
            prime[j] = False

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for elem in arr:
    if prime[elem]:
        cnt += 1

print(cnt)