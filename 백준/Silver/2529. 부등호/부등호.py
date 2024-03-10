def backtrack(idx, prev, nums, used):
    global max_val, min_val, signs

    if idx == len(signs) + 1:
        num = int("".join(map(str,  nums)))
        max_val = max(max_val, num)
        min_val = min(min_val, num)
        return

    for i in range(10):
        if used[i]:
            continue
    
        if idx == 0 or (signs[idx -1] == "<" and prev < i) or (signs[idx -1] == ">" and prev > i):
            used[i] = True
            backtrack(idx + 1, i, nums + [i], used)
            used[i] = False
        
n = int(input())
signs = input().split()
max_val = -1
min_val = 1e10

backtrack(0, 0, [], [False] * 10)
print(max_val, min_val if len(str(min_val)) != n else "0" + str(min_val), sep="\n")
