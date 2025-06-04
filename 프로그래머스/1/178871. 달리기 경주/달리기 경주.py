def solution(players, callings):
    answer = []
    score = {}
    for p in range(len(players)):
        score[players[p]] = p
        answer.append(players[p])
        
    for c in callings:
        s = score[c]
        score[c] -= 1
        score[answer[s-1]] = s
        answer[s],answer[s-1] = answer[s-1],answer[s]
        
    return answer