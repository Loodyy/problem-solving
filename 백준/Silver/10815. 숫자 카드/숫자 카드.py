MAX = 10_000_000
A = [0] * 2 * MAX
input()
for num in map(int, input().split()):
    A[num+MAX] = 1
input()
print(*map(lambda x: A[int(x)+MAX], input().split()))