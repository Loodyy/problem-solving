def solution(today, terms, privacies):
    answer = []
    
    termDict = dict()
    for term in terms:
        info, dueMonth = term.split()
        termDict[info] = int(dueMonth)
        
    for idx, privacy in enumerate(privacies):
        date, term = privacy.split()
        if isExpired(today, date, termDict[term]):
            answer.append(idx + 1)
    
    return answer

def isExpired(today, started, month):
    ty, tm, td = map(int, today.split("."))
    dy, dm, dd = getDue(started, month)
    
    return ty * 28 * 12 + tm * 28 + td > dy * 28 * 12 + dm * 28 + dd
    
def getDue(prev, month):
    y, m, d = map(int, prev.split("."))
    if d == 1:
        m -= 1
        d = 28
    else :
        d -= 1
    
    m += month
    if m > 12:
        m -= 12
        y += 1
        
    return y, m, d