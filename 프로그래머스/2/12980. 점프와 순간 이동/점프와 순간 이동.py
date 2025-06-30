def solution(n):
    ans = 0
    while n > 3:
        if n % 2 == 0:
            n = n//2
        else:
            n -= 1
            ans += 1
        
    if n == 3:
        ans += 2
    else: # n == 1 or n == 2
        ans += 1

    return ans