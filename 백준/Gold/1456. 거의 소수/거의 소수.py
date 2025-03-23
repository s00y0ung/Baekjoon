def solve():
    A, B = map(int, input().split())

    prime = [True] * (int(B ** 0.5)+1)
    prime[1] = False
    almost_prime_cnt = 0

    for i in range(2, int(B ** 0.5)+1):
        if prime[i] == 0:
            continue
        for j in range(i+i, int(B**0.5)+1, i):
            prime[j] = False

        tmp = i*i
        while tmp <= B:
            if A <= tmp:
                almost_prime_cnt += 1
            tmp = tmp * i

    print(almost_prime_cnt)

solve()