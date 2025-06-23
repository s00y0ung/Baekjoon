def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

def solution(n, m):
    c = gcd(n, m)
    answer = [c, n*m//c]
    return answer