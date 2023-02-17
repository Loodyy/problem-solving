# 42
# 0101010

# 1 -> 1
# 2 -> 3
# 3 -> 7
# 4 -> 15
# 5 -> 31

def getNodeNum(currNum):
    for i in range(int(1e9)):
        temp = 2 ** i
        if temp <= currNum < temp * 2:
            return temp * 2 - 1
    return 0

def dec2bin(n):
    binStr = str(bin(n))
    binStr = binStr[2:]
    return binStr.zfill(getNodeNum(len(binStr)))

def solve(binString) -> bool:
    n = len(binString)
    if n == 1:
        return True
    
    if isBinaryTree(binString):
        return False
    
    l, r = binString[:n // 2], binString[n // 2 + 1:]
    return solve(l) and solve(r)

def isBinaryTree(binString):
    n = len(binString)
    l, r = binString[:n // 2], binString[n // 2 + 1:]

    m = getMid(binString)
    lm, rm = getMid(l), getMid(r)
    
    return (lm == "1" or rm == "1") and m == "0"
    
def getMid(binString):
    n = len(binString)
    return binString[n // 2]
   

def solution(numbers):
    res = []
    for num in numbers:
        binString = dec2bin(num)
        res.append(+solve(binString))
    
    return res