def solution(players, callings):
    idxs = dict()
    for i, p in enumerate(players):
        idxs[p] = i
    
    for c in callings:
        idx = idxs[c]
        prev = players[idx - 1]
        idxs[prev], idxs[c] = idx, idx - 1
        players[idx], players[idx - 1] = prev, c
    
    return players