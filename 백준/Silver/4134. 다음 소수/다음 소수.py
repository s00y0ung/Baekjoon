import sys
input = sys.stdin.readline

def check(x):
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            return False
    return True

N = int(input())
prime = [0 for _ in range(4 * 1000000 + 1)]

for _ in range(N):
    k = int(input())
    while True:
        if k == 1 or k == 0:
            print(2)
            break
        
        if check(k):
            print(k)
            break
        else:
            k += 1