def solution(n, m, x, y, r, c, k):
    answer = ""
    n, m, sx, sy, ex, ey = m, n, y - 1, x - 1, c - 1, r - 1
    
    direction = [(0, 1, "d"), (-1, 0, "l"), (1, 0, "r"), (0, -1, "u")]
    # d < l < r < u
    dx, dy = ex - sx, ey - sy
    dist = abs(dx) + abs(dy)
    tdist = k - dist
    if tdist < 0 or tdist % 2 != 0:
        return "impossible"
    
    cx, cy = sx, sy
    tdist //= 2
    targetDir = []
    dirDict = { "r": 0, "l": 0, "u": 0, "d": 0 }
    if dx > 0:
        dirDict["r"] = dx
    else:
        dirDict["l"] = -dx
    if dy > 0:
        dirDict["d"] = dy
    else:
        dirDict["u"] = -dy
    for _ in range(k):
        for xx, yy, dir in direction:
            tx, ty = cx + xx, cy + yy
            if not isRange(tx, ty, n, m):
                continue
            if dirDict[dir]:
                dirDict[dir] -= 1
                answer += dir
                cx, cy = tx, ty
                break
            elif tdist:
                answer += dir
                cx, cy = tx, ty
                tdist -= 1
                dirDict[getRdir(dir)] += 1
                break
            
    return answer

def getRdir(dir):
    temp = { "l": "r", "r": "l", "u": "d", "d": "u" }
    return temp[dir]

def isRange(x, y, n, m):
    return 0 <= x < n and 0 <= y < m 