def solution(n, k):
    answer = []
   
    arr = list(range(1, n+1))
    k -= 1
    
    while arr:
        div, mod = divmod(k, facto(n-1))
        answer.append(arr[div])
        arr.pop(div)
        
        k = mod
        n -= 1
    return answer
    
def facto(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res