import sys
input = sys.stdin.readline

def solve():

    for i in range(1, 10001):
        if count[i] > 0:
            for _ in range(count[i]):
                print(i)
    return

if __name__ == "__main__":

    n = int(input())
    count = [0] * (10001)

    for _ in range(n):
        count[int(input())] += 1

    solve()