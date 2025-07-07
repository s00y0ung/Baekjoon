def solution(n):
    if n % 2 == 1:
        return 0
    ans = [0 for i in range(5001)]
    ans[2] = 3
    ans[4] = 11
    for i in range(6, n+1, 2):
        ans[i] = ans[i-2]*3
        for j in range(i-4, 0, -2):
            ans[i] += (ans[j]*2)
            
        ans[i] = (ans[i]+2) % 1000000007
    return ans[n] % 1000000007