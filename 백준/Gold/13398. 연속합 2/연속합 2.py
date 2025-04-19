import sys
input = sys.stdin.readline

N = int(input())
n_list = list(map(int, input().split()))
prefix_l = [0] * (N)
prefix_r = [0] * (N)
max_n = n_list[0]

prefix_l[0] = n_list[0]
for i in range(1, N):
    prefix_l[i] = max(prefix_l[i-1]+n_list[i], n_list[i])
    if max_n < prefix_l[i]:
        max_n = prefix_l[i]

prefix_r[N-1] = n_list[N-1]
for j in range(N-2,-1,-1):
    prefix_r[j] = max(prefix_r[j+1]+n_list[j], n_list[j])

for idx in range(1,N-1):
    if max_n < prefix_l[idx-1] + prefix_r[idx+1]:
        max_n = prefix_l[idx-1] + prefix_r[idx+1]
print(max_n)