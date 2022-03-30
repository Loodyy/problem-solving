import sys
from itertools import combinations
input = sys.stdin.readline

def solve():
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_v = sum(map(sum, arr))
    result = []

    for x in com:
        y = [i for i in range(1, n+1) if i not in x]

        if x[0] == 1:
            temp1, temp2 = 0, 0
            for i in x:
                for j in x:
                    temp1 += arr[i-1][j-1]
            for i in y:
                for j in y:
                    temp2 += arr[i-1][j-1]
            
            result.append(abs(temp1-temp2))
    
    print(min(result))
    return

if __name__ == "__main__":
    n = int(input())
    team = [i for i in range(1, n+1)]
    com = list(combinations(team, int(n/2)))

    solve()