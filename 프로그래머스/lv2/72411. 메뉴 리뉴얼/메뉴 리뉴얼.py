from itertools import combinations as com
from collections import defaultdict

def solution(orders, course) -> list:
    res = []
    
    for cnt in course:
        courseList = getCourseList(orders, cnt)
        res.extend(courseList)

    res.sort()
    return res

def getCourseList(orders, cnt):
    candidateDict = defaultdict(int)
    for order in orders:
        canList = com(sorted(list(order)), cnt)
        for can in canList:
            candidateDict["".join(can)] += 1

    res = []  
    LIMIT = 2      
    maxCnt = -1
    for course, cnt in candidateDict.items():
        if cnt > maxCnt and cnt >= LIMIT:
            res = [course]
            maxCnt = cnt
        elif cnt == maxCnt:
            res.append(course)
    
    return res