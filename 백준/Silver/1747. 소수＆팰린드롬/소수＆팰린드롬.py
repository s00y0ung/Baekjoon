def solve():
    N = int(input())
    prime = [i for i in range(1003002)]
    prime[0] = 0
    prime[1] = 0

    # 소수 구하기
    for i in range(2,len(prime)):

        if prime[i] != 0:
            for j in range(i+i, len(prime), i):
                prime[j] = 0

            # 팰린드롬
            if prime[i] >= N:
                s = str(i)
                if s == s[::-1]:
                    print(s)
                    break


solve()
