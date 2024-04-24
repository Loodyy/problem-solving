def is_match(arr):
    if arr[:2] == "01":
        if len(arr) == 2:
            return True
        return is_match(arr[2:])
    elif arr[:2] == "10":
        z_cnt, o_cnt = 0, 0
        for i in range(2, len(arr)):
            if arr[i] == "0":
                z_cnt += 1
                if o_cnt == 1:
                    return is_match(arr[i:])
                elif o_cnt >= 2:
                    return is_match(arr[i:]) or is_match(arr[i-1:])
            else:
                o_cnt += 1
                if z_cnt == 0:
                    return False
        if z_cnt > 0 and o_cnt > 0:
            return True
    else:
        return False

T = int(input())
for _ in range(T):
    arr = input()
    print("YES" if is_match(arr) else "NO")