def solution(n, k):
    answer = 0
    s = ''
    while n != 0:
        s = str(n%k) + s
        n = n//k

    s = s.split('0')    
    print(s)
    for c in s:
        if c == '' or c =='1':
            continue
        a = int(c)
        for i in range(2, int(a**0.5)+1):
            if a % i == 0:
                answer -= 1
                break
        answer += 1
        
    return answer