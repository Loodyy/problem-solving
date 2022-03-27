import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(10)]

def solve():
    now = 0
    result = 0
    for i in range(10):
        now += arr[i]
        if now >= 100:
            pre = now - arr[i]
            if now - 100 <= 100 - pre:
                result = now
            else: result = pre
            return result
    result = now # 합이 100이 안됐을 때
    return result

print(solve())