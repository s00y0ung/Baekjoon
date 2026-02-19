import sys
input = sys.stdin.readline

N,M = map(int, input().split())
a_list = list(map(int, input().split()))
s_list = [0]*N
s_list[0] = a_list[0]
for i in range(1,N):
    s_list[i] = a_list[i]+s_list[i-1]
for i in range(M):
    start, end = map(int, input().split())
    if start == 1:
        print(s_list[end-1])
    else:
        print(s_list[end-1]-s_list[start-2])