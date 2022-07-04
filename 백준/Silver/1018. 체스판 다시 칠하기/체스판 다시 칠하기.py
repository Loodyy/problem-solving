def solve():
    minV = int(1e9)
    for i in range(n-7):
        for j in range(m-7):
            minV = min(minV, count_false(j, i))

    return minV

def count_false(x, y):
    cnt1, cnt2 = 0, 0
    for i in range(8):
        for j in range(8):
            if arr[i+y][j+x] != comp1[i][j]:
                cnt1 += 1
            if arr[i+y][j+x] != comp2[i][j]:
                cnt2 += 1

    return min(cnt1, cnt2)     

comp1 = ["BWBWBWBW", "WBWBWBWB"] * 4
comp2 = ["WBWBWBWB", "BWBWBWBW"] * 4
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
print(solve())