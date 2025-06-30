def solution(n):
    answer = 1
    cnt = bin(n).count('1')
    while bin(n+answer).count('1') != cnt:
        answer += 1
    return answer+n