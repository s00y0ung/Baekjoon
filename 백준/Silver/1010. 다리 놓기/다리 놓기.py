import sys
input = sys.stdin.readline

def factorial(a):
    ans = 1
    for idx in range(1, a+1):
        ans = ans * idx
    return ans

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(factorial(b) // (factorial(b-a) * factorial(a)))
