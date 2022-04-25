from collections import deque

def solve(p, arr):
    
    check_re = False
    for x in p: # 100,000
        if x == "R":
            check_re = True if not check_re else False
        else:
            if len(arr):
                if not check_re:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print("error")
                return
    
    if check_re:
        arr.reverse()
    print("[", end='')
    for i in range(len(arr)):
        if i != len(arr)-1: print(arr[i], end=',')
        else: print(arr[i], end='')
    print("]")
    return

if __name__ == "__main__":

    t = int(input())

    for _ in range(t): # 100

        p = input()
        n = int(input())
        temp = input()
        tmp = temp[1:len(temp)-1]
        if len(tmp): 
            arr = deque(list(map(int, tmp.split(','))))
            
        else:
            arr = deque()
        solve(p, arr)