def solution(bandage, health, attacks):
    answer = health
    attacks.append([0])
    for t in range(len(attacks)-1):
        band_time = attacks[t][0] - attacks[t-1][0] - 1
        bt = band_time // bandage[0]
        answer = answer + bt * bandage[2] + band_time * bandage[1]
        if answer > health:
            answer = health

        answer -= attacks[t][1]
        if answer <= 0:
            return -1
        
    return answer
