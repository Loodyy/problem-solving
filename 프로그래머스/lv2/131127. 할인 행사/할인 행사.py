from collections import defaultdict

def solution(want, number, discount):
    rangeLen, discountLen = 10, len(discount)
    
    itemDict = defaultdict(int)
    for i in range(rangeLen):
        itemDict[discount[i]] += 1
    
    answer = 0
    day = 0
    while day < discountLen:
        if (isMatched(want, number, itemDict)):
            answer += 1 
        itemDict[discount[day]] -= 1
        if (day + rangeLen) < discountLen:
            itemDict[discount[day + rangeLen]] += 1
        day += 1
        
    return answer

def isMatched(want, number, itemDict):
    l = len(want)
    for i in range(l):
        name = want[i]
        num = number[i]
        if (itemDict.get(name) and itemDict.get(name) >= num):
            continue
        return False
    return True
