def get_prime(n):
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return 0
    return 1

def backTracking(n, depth, N):

    if depth == N:
        if get_prime(n):
            print(n)
        return

    for k in [1,3,7,9]:
        if get_prime(n*10+k):
            backTracking(n*10+k, depth+1, N)

N = int(input())
for i in [2,3,5,7]:
    backTracking(i, 1, N)