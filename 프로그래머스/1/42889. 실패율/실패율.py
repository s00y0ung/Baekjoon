def solution(N, stages):
    answer = []
    challenge = [0 for i in range(N + 1)]
    for s in stages:
        challenge[s-1] += 1

    total = len(stages)
    for c in range(N):
        if total == 0:
            answer.append([0,c+1])
        else:
            answer.append([challenge[c] / total, c+1])
            total -= challenge[c]
        
        
    answer = sorted(answer, key=lambda x: (-x[0], x[1]))
    answer = [x[1] for x in answer]
    
    return answer
