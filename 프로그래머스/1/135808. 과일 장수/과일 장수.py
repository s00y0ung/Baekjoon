def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    
    for s in range(m-1, len(score), m):
        answer = answer + (score[s] * m)
    
    return answer