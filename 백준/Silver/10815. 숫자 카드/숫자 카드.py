input()
num_set = set(map(int, input().split()))
input()
print(*map(lambda x: 1 if int(x) in num_set else 0, input().split()))
