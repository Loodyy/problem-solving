import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    b, c = map(int, input().split())
    result = n

    for i in arr:
        if i - b > 0:
            if (i-b)%c > 0:
                result += 1
            result += (i-b)//c

    return result

print(solve())