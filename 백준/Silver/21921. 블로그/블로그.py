n, x = map(int, input().split())
nums = list(map(int, input().split()))


tsum = sum(nums[:x])
max = tsum
lasted = 1

for i in range(x, n):
    curr = tsum - nums[i - x] + nums[i]
    if curr > max:
        max = curr
        lasted = 1
    elif curr == max:
        lasted += 1
    tsum = curr

if max == 0:
    print("SAD")
else:
    print(max)
    print(lasted)