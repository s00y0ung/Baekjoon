import sys
input = sys.stdin.readline

def check(x):
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            return False
    return True

N = int(input())

for _ in range(N):
    k = int(input())
    if k == 1 or k == 0 or k == 2:
        print(2)
        continue
    
    if k % 2 == 0:
        k += 1

    while True:
        if check(k):
            print(k)
            break
        else:
            k += 2