def solve():
    N = int(input())
    ans = N
    p = []

    # 서로소 개수 구하기
    for i in range(2, int(N**0.5)+1):
        if ans % i == 0:
            p.append(i)
            while ans % i == 0:
                ans = ans // i
            if ans == 1:
                break

    if ans != 1:
        p.append(ans)
    ans = N
    for pidx in p:
        ans = ans - ans // pidx
    print(ans)

solve()