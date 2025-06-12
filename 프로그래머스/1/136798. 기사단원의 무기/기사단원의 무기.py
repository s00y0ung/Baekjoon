def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        t = 0
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                t += 2
        if i % (i**0.5) == 0:
            t -= 1
        if t > limit:
            t = power
            
        answer = answer + t
    return answer