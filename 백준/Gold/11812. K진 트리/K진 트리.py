import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def solve(a, b):

    result = 0

    if k == 1:
        result = abs(a-b)
    else:
        while a != b:
            if a < b:
                b = (b-2)//k+1
            else:
                a = (a-2)//k+1
            result += 1

    print(result)
    return

if __name__ == "__main__":

    n, k, q = map(int, input().split())

    for _ in range(q):
        a, b = map(int, input().split())
        solve(a, b)
