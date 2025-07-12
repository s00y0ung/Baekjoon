N = int(input())
if N == 1 or N ==2:
    print(1)
else:
    ans = 1
    s,e = 1,1
    total = 1
    while s <= e <= N//2+1:
        if total < N:
            e += 1
            total += e
        elif total > N:
            total -= s
            s += 1
        else:
            e += 1
            total = total + e -s
            s += 1
            ans += 1

    print(ans)
