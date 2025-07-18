def solution(cards):
    answer = []
    cards = [0] + cards
    
    for c in range(1, len(cards)):
        if cards[c] == -1:
            continue
        cnt = 0
        while cards[c] != -1:
            tmp = cards[c]
            cards[c] = -1
            c = tmp
            cnt += 1
        answer.append(cnt)
        
    if len(answer) == 1:
        return 0
    answer.sort()

    return answer[-1]*answer[-2]
