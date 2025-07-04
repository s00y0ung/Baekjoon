from fractions import gcd

def solution(arr):
    answer = arr[0]
    for a in arr[1:]:
        tmp = gcd(a, answer)
        answer = a*answer//tmp
        
    return answer