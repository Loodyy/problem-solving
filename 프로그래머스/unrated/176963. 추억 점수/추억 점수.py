from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    temp = defaultdict(int)
    for n, y in zip(name, yearning):
        temp[n] = y
    
    for p in photo:
        score = sum(map(lambda x: temp[x], p))
        answer.append(score)

    return answer