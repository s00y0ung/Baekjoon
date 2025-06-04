def solution(players, m, k):
    cnt = [0 for i in range(24)]
    cnt[0] = players[0] // m
    answer = cnt[0]
    cnt[k] = -cnt[0]
    
    for i in range(1,24):
        cnt[i] = cnt[i-1]+cnt[i]
        #서버 증설이 필요한 경우
        if players[i] >= (cnt[i]+1)*m:
            c = (players[i]//m) - cnt[i]
            answer += c
            cnt[i] += c
            if i+k < 24:
                cnt[i+k] -= c
        
    return answer