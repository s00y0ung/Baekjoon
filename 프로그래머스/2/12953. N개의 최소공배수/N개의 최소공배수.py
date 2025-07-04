def get_gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

def solution(arr):
    answer = arr[0]
    for a in arr[1:]:
        tmp = get_gcd(a, answer)
        answer = a*answer//tmp
        
    return answer