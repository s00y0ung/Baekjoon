import sys
import math
input = sys.stdin.readline

N,M,K =  map(int, input().split())
#n+1 H m == math.comb(N+M, M)
total = math.comb(N+M, M)
if K > total:
    print(-1)
else:
    result = []
    while N > 0 and M > 0:
        a = math.comb(N+M-1, M)
        if a >= K:
            result.append('a')
            N -= 1
        else:
            result.append('z')
            M -= 1
            K = K - a

    if M != 0:
        for i in range(M):
            result.append('z')
    else:
        for i in range(N):
            result.append('a')
    print(''.join(result))