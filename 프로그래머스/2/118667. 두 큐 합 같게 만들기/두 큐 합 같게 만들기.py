def solution(queue1, queue2):
    answer = 0
    q = queue1 + queue2
    total = (sum(queue1) + sum(queue2))
    if total % 2 == 1:
        return -1
    
    total = total // 2
    s, e = 0, len(queue1) - 1
    sm = sum(queue1)
    
    while s <= e:
        if sm > total:
            sm -= q[s]
            s += 1
        elif sm < total:
            e += 1
            if e >= len(q):
                answer = -1
                break
            sm += q[e]
        else:
            break
        answer += 1

    if s > e:
        answer = -1

    return answer