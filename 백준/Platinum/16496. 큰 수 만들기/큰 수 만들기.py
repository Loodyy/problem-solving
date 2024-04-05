from functools import cmp_to_key

N = int(input())
A = list(input().split())

def key_func(x, y):
    return int(x+y) - int(y+x)

A.sort(key=cmp_to_key(key_func), reverse=True)

ans = "".join(A)
print(ans if int(ans) != 0 else 0)