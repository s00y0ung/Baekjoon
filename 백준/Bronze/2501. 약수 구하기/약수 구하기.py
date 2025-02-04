N, K = map(int, input().split())

N_list = [0]
for i in range(1, N+1):
    if N % i == 0:
        N_list.append(i)

if len(N_list)-1 < K:
    print(0)
else:
    print(N_list[K])