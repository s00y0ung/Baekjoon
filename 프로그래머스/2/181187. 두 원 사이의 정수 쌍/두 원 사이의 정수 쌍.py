import math

def solution(r1, r2):
    answer = 0
    
    for x in range(1,r2+1):
        high = int(math.sqrt(r2**2 - x**2))
        if x < r1:
            low = math.ceil(math.sqrt(r1**2 - x**2))
        else:
            low = 0
        answer = answer + high - low + 1
    return answer*4