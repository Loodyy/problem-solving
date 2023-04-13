def solution(cap, n, deliveries, pickups):
    dist = 0
    nonZeroDel = []
    nonZeroPick = []
    for i in range(n):
        if deliveries[i]:
            nonZeroDel.append([i, deliveries[i]])
        if pickups[i]:
            nonZeroPick.append([i, pickups[i]])
            
    while True:
        checkIdx = n
        delCap = cap
        pickCap = cap

        currDist = -1
        if nonZeroDel:
            currDist = max(currDist, nonZeroDel[-1][0])
        if nonZeroPick:
            currDist = max(currDist, nonZeroPick[-1][0])  
        
        if currDist == -1:
            break
        
        while nonZeroDel and delCap > 0:
            d = nonZeroDel[-1][1]
            if d > delCap:
                nonZeroDel[-1][1] -= delCap
                delCap = 0
            else:
                nonZeroDel.pop()
                delCap -= d
                
        while nonZeroPick and pickCap > 0:
            p = nonZeroPick[-1][1]
            if p > pickCap:
                nonZeroPick[-1][1] -= pickCap
                pickCap = 0
            else:
                nonZeroPick.pop()
                pickCap -= p
        
        dist += 2 * (currDist + 1)
        checkIdx = currDist
            
    return dist