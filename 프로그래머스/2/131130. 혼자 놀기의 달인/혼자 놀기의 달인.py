def solution(cards):
    answer = []
    cards = [0] + cards
    visited = [0 for i in range(len(cards))]
    
    for c in cards[1:]:
        if visited[c] == 1:
            continue
        cnt = 0
        while visited[c] == 0:
            visited[c] = 1
            c = cards[c]
            cnt += 1
        answer.append(cnt)
        
    if len(answer) == 1:
        return 0
    answer.sort()
    return answer[-1]*answer[-2]
