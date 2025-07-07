def solution(n):
    prev, pprev = 1,0
    answer = 0
    for i in range(n):
        answer = prev + pprev
        prev, pprev = answer, prev
    return answer % 1000000007