import sys
input = sys.stdin.readline 

N = int(input())
n_list = []
for _ in range(N):
    n = int(input())
    n_list.append(n)

n_list.sort()
s_list = [1 for _ in range(N)]
s_max = 1
for i in range(1,N):
    if n_list[i] == n_list[i-1]:
        s_list[i] = s_list[i-1] + 1
    if s_list[i] > s_max:
        s_max = s_list[i]
flag = 0
k = 0
for i in range(N):
    if s_max == s_list[i]:
        if flag == 1:
            k = n_list[i]
            break
        k = n_list[i]
        flag = 1

maxN = n_list[-1]
minN = n_list[0]

print(round(sum(n_list)/N), n_list[N//2] , k ,maxN-minN, sep = '\n')