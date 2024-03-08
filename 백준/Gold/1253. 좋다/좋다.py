n = int(input())
nums = list(map(int, input().split()))
nums.sort()

answer = 0
for i in range(n):
    targ = nums[i]
    l, r = 0, n - 1
    while l < r:
        if nums[l] + nums[r] == targ:
            if l == i:
                l += 1
            elif r == i:
                r -= 1
            else:
                answer += 1
                break
        elif nums[l] + nums[r] > targ:
            r -= 1
        else:
            l += 1

print(answer)