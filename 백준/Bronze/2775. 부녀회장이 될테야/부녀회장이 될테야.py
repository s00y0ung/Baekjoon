import sys
input = sys.stdin.readline

T = int(input())
a = [[0]*15 for _ in range(15)]
a[0] = [i for i in range(15)]

for i in range(1, 15):
    for j in range(1, 15):
        a[i][j] = a[i][j-1] + a[i-1][j]

for _ in range(T):
    N = int(input())
    K = int(input())
    print(a[N][K])