import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
prefix_sum = [0 for i in range(N+1)]
s = 0

for i in range(N):
    arr.append(list(map(int, input().split())))
    
    prefix = 0
    prefix_sum.append(0)
    for j in range(N):
        if i == 0:
            s = s + arr[i][j]
            prefix_sum.append(s)
            continue
            
        prefix = prefix + arr[i][j]
        prefix_sum.append(prefix + prefix_sum[(i)*(1+N)+(j+1)])

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    tmp1 = prefix_sum[(N+1)*(x1-1) + (y1-1)]
    tmp2 = prefix_sum[(N+1)*(x1-1) + (y2)]
    tmp3 = prefix_sum[(N+1)*(x2) + (y1-1)]
    tmp4 = prefix_sum[(N+1)*(x2) + (y2)]
    
    print(tmp4 - tmp2 - tmp3 + tmp1)