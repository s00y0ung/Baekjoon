def solution(bandage, health, attacks):
    answer = health
    at = 0
    bt = 0
    for t in range(attacks[-1][0] + 1):
        if t == attacks[at][0]:
            answer -= attacks[at][1]
            at += 1
            bt = 0
            if answer <= 0:
                return -1
        else:
            bt += 1
            answer += bandage[1]
            if answer >= health:
                answer = health
                continue
            if bt == bandage[0]:
                bt = 0
                answer += bandage[2]  
        
    return answer