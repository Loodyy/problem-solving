T = int(input())

for _ in range(T):
    N, K, T, M = map(int, input().split())

    score_map = { idx: { 
        "meta" : { "accept_cnt": 0, "last_accept": 0, "total_score": 0 }, 
        "score_board": { j: 0 for j in range(1, K+1)} # (prob_num, score)
        } for idx in range(1, N+1) }
    for log_idx in range(M):
        I, J, S = map(int, input().split())
        score_map[I]["meta"]["accept_cnt"] += 1
        score_map[I]["meta"]["last_accept"] = log_idx
        prev_max = score_map[I]["score_board"][J]
        if prev_max < S:
            score_map[I]["score_board"][J] = S
            score_map[I]["meta"]["total_score"] += S - prev_max

    me = score_map[T]["meta"]
    rank = 0
    for idx in range(1, N+1):
        if idx == T:
            continue
        other = score_map[idx]["meta"]
        if other["total_score"] > me["total_score"]:
            rank += 1
        elif other["total_score"] == me["total_score"]:
            if other["accept_cnt"] < me["accept_cnt"]:
                rank += 1
            elif other["accept_cnt"] == me["accept_cnt"]:
                if other["last_accept"] < me["last_accept"]:
                    rank += 1
        
    print(rank+1)