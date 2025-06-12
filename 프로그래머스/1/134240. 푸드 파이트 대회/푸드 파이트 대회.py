def solution(food):
    answer = ''
    for idx,n in enumerate(food):
        answer = answer +  str(idx) * (n//2)
    answer = answer + '0' + answer[::-1]
    return answer