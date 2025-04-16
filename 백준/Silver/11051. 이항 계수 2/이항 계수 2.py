import sys
input = sys.stdin.readline

def factorial(a):
    ans = 1
    for i in range(1,a+1):
        ans *= i
    return ans

N, K = map(int, input().split())
print(factorial(N) // (factorial(K) * factorial(N-K)) % 10007)