def solution(cacheSize, cities):
    answer = 0
    cq = []
    for c in cities:
        if c.lower() in cq:
            answer += 1
            cq.remove(c.lower())
            cq.append(c.lower())
        else:
            answer += 5
            cq.append(c.lower())
            if len(cq) > cacheSize:
                cq.pop(0)
        
    return answer