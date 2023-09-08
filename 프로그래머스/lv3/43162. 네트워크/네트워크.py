from collections import deque

def solution(n, computers):
    nodeLen = len(computers)
    isVisit = [False for _ in range(nodeLen)]
    
    linkCnt = 0
    while True:
        dq = deque()
        src = getNextSrc(isVisit)
        if src < 0:
            break
        dq.append(src)
        isVisit[src] = True
        while dq:
            cNode = dq.popleft()
            for nNode, isConn in enumerate(computers[cNode]):
                if nNode == cNode:
                    continue
                if (isConn == 1 and not isVisit[nNode]):
                    dq.append(nNode)
                    isVisit[nNode] = True
        linkCnt += 1
        
    return linkCnt

def getNextSrc(isVisit):
    for i, bool in enumerate(isVisit):
        if (not bool):
            return i
    return -1
        
    