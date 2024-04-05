N = int(input())
A = list(input().split())

A.sort(key=lambda x: x * 9, reverse=True)

ans = "".join(A)
print(ans if int(ans) != 0 else 0)