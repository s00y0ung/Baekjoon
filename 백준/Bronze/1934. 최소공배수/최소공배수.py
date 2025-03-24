import sys
input = sys.stdin.readline

def solve():
    A, B = map(int, input().split())
    m,n = A,B
    while n != 0:
        m,n = n, m%n
    # 최대 공약수 == m
    print(A*B//m)

T = int(input())
for i in range(T):
    solve()