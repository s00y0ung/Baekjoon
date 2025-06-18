def solution(absolutes, signs):
    
    for s in range(len(signs)):
        if not signs[s]:
            absolutes[s] *= -1
    answer = sum(absolutes)
    
    return answer