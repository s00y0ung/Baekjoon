def solution(n, m, section):
    answer = 1
    prev = section[0]
    
    for s in section:
        if s - prev >= m:
            prev = s
            answer += 1
    
    return answer