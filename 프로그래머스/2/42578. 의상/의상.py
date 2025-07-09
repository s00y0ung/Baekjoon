def solution(clothes):
    answer = 1
    cdic = {}
    for c in clothes:
        if c[1] in cdic:
            cdic[c[1]].append(c[0])
        else:
            cdic[c[1]] = [c[0]]
    for k, v in cdic.items():
        answer = answer * (len(v)+1)      
    answer -= 1
    return answer