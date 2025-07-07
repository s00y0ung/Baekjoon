def solution(n,a,b):
    answer = 0
    
    while b != a:
        if b % 2 == 1:
            b += 1
        if a % 2 == 1:
            a += 1
        a = a // 2
        b = b // 2
        answer += 1

    return answer