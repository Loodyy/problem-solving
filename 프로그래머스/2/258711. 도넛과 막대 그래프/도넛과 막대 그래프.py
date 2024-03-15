def solution(edges):
    node_idxs = set()
    for s, e in edges:
        node_idxs.add(s)
        node_idxs.add(e)
    node_idx_list = sorted(list(node_idxs))    
    
    nodes = {i: {"in": 0, "out": 0} for i in node_idx_list}
    for s, e in edges:
        nodes[s]["out"] += 1
        nodes[e]["in"] += 1
        
    created_node = None
    line_cnt = 0
    eight_cnt = 0
    for i in node_idx_list:
        node = nodes[i]
        if node["in"] == 0 and node["out"] >= 2:
            created_node = i
        if node["out"] == 0:
            line_cnt += 1
        if node["in"] >= 2 and node["out"] == 2:
            eight_cnt += 1
    
    total_cnt = nodes[created_node]["out"]
    return [created_node, total_cnt - line_cnt - eight_cnt, line_cnt, eight_cnt]
