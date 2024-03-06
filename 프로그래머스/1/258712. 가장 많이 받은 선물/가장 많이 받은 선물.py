def solution(friends, gifts):
    n = len(friends)
    index = { f: i for i, f in enumerate(friends) }
        
    gift_score = [0] * n
    answer = [0] * n
    table = [[0 for _ in range(n)] for _ in range(n)]
    for gift in gifts:
        s, e = gift.split()
        table[index[s]][index[e]] += 1
        gift_score[index[s]] += 1
        gift_score[index[e]] -= 1
        
    for i in range(n):
        for j in range(n):
            if table[i][j] > table[j][i]:
                answer[i] += 1
            if table[i][j] == table[j][i]:
                if gift_score[i] > gift_score[j]:
                    answer[i] += 1
    return max(answer) 