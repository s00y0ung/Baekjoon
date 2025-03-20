def solve():
    M,N = map(int, input().split())

    prime_list = [True] * (N+1)
    prime_list[1] = False

    for i in range(2,int(N**0.5)+1):
        if prime_list[i]:
            k = 2
            while i*k <= N:
                prime_list[i*k] = False
                k += 1

    for i in range(M, N+1):
        if prime_list[i]:
            print(i)

solve()