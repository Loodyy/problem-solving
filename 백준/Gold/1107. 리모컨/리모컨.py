def solve(keys, nums):
    global minV

    if len(nums) and leng-1 <= len(nums) <= leng+1:
        minV = min(minV, len(nums)+abs(targ-int("".join(nums))))
        if len(nums) == leng+1:
            return

    for key in keys:
        nums.append(str(key))
        solve(keys, nums)
        nums.pop()

targ = int(input())
m = int(input())
temp = set()
if m != 0:
    temp = set(map(int, input().split()))
keys = [x for x in range(10) if x not in temp]

leng = len(str(targ))
minV = int(1e9)
solve(keys, [])

print(min(minV, abs(targ-100)))