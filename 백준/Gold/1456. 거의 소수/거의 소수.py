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

    for i in range(2, int(B ** 0.5)+1):
        if prime[i]:
            tmp = i
            while tmp <= B:
                tmp *= i
                if A <= tmp <= B:
                    almost_prime_cnt += 1

    print(almost_prime_cnt)

solve()