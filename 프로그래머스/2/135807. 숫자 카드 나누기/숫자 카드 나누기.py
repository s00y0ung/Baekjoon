def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solution(arrayA, arrayB):
    gcd_a = arrayA[0]
    for a in arrayA:
        gcd_a = gcd(gcd_a, a)
    
    gcd_b = arrayB[0]
    for b in arrayB:
        gcd_b = gcd(gcd_b, b)
        
    for b in arrayB:
        if b % gcd_a == 0:
            gcd_a = 0
            break
    for a in arrayA:
        if a % gcd_b == 0:
            gcd_b = 0
            break
            
    return max(gcd_a, gcd_b)