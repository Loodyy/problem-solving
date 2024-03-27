T = int(input())
for _ in range(T):
    temp = list(map(int, input().split()))
    idx, heights = temp[0], temp[1:]
    cnt = 0

    pivot = 0
    while pivot < len(heights):
        for i in range(pivot):
            if heights[i] > heights[pivot]:
                cnt += pivot - i
                heights.insert(i, heights.pop(pivot))
                break
        pivot += 1

    print(idx, cnt)