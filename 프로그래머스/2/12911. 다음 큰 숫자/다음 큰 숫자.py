def solution(n):
    answer = 1
    cnt = str(format(n, 'b')).count('1')
    while str(format(n+answer,'b')).count('1') != cnt:
        answer += 1
    return answer+n