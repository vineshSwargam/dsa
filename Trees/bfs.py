def gen_parentheses(pairs: int):
    queue = [('', 0, 0)]
    res = []

    while queue:
        cur, ou, cu = queue.pop(0)
        if len(cur) == pairs*2:
            res.append(cur)
        else:
            if ou < pairs:
                queue.append((cur+'(', ou+1, cu))
            if cu < ou:
                queue.append((cur+')', ou, cu+1))
        
    return res

print(gen_parentheses(3))