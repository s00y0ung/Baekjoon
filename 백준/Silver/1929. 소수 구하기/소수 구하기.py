M,N = map(int, input().split())

prime_list = [i for i in range(N+1)]
prime_list[1] = 0
for i in range(1,N+1):
    if prime_list[i] == 0:
        continue

    k = 2
    while i*k <= N:
        prime_list[i*k] = 0
        k += 1

for i in range(M, N+1):
    if prime_list[i] != 0:
        print(prime_list[i])