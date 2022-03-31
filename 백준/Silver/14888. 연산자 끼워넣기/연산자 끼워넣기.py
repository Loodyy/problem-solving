def solve():
    comp = []
    for temp in perm:
        if comp == temp:
            continue
        comp = temp
        result = nums[0]
        for i, operators in enumerate(temp):
            if operators == 0: result += nums[i+1]
            elif operators == 1: result -= nums[i+1]
            elif operators == 2: result *= nums[i+1]
            else: 
                if result < 0:
                    result = -result// nums[i+1]
                    result *= -1
                else: result = result // nums[i+1]
        result_num.append(result)
 
    return max(result_num), min(result_num)

def permu(cnt):
    if cnt == len(oper):
        temp = [x for x in list]
        perm.append(temp)
        return

    for i, val in enumerate(oper):
        if visited[i]:
            continue
        visited[i] = True
        list.append(val)
        permu(cnt+1)
        list.pop()
        visited[i] = False

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split())) 
    op = list(map(int, input().split())) 
    oper = []
    for i in range(4):
        leng = op[i]
        if i == 0:
            for j in range(leng): oper.append(i)
        elif i == 1:
            for j in range(leng): oper.append(i)
        elif i == 2:
            for j in range(leng): oper.append(i)
        else:
            for j in range(leng): oper.append(i)

    visited = [False] * len(oper)
    list = []
    perm = []
    permu(0)

    result_num = []
    a, b = solve()

    print(a)
    print(b)    