def solve(idx, temp):
    if idx == n:
        result.append(temp)
        return
    else:
        if op[0] > 0:
            op[0] -= 1
            solve(idx+1, temp+nums[idx])
            op[0] += 1
        
        if op[1] > 0:
            op[1] -= 1
            solve(idx+1, temp-nums[idx])
            op[1] += 1
        
        if op[2] > 0:
            op[2] -= 1
            solve(idx+1, temp*nums[idx])
            op[2] += 1

        if op[3] > 0:
            op[3] -= 1
            if temp < 0:
                temp = -(-temp//nums[idx])
            else: temp //= nums[idx]
            solve(idx+1, temp)
            op[3] += 1
        return

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split())) 
    op = list(map(int, input().split())) 
    result = []
    temp = nums[0]
    solve(1, temp)

    print(max(result))
    print(min(result))