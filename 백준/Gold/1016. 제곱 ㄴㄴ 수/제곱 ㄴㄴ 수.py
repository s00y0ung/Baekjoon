def solve():
    MIN, MAX = map(int, input().split())
    prime = [ i for i in range(MIN, MAX+1)]

    for i in range(2, int(MAX ** 0.5)+1):
        s = i*i
        s_idx = (MIN//s) * s
        for j in range(s_idx, MAX+1, i*i):
            if j >= MIN:
                prime[j-MIN] = 0

    cnt = 0
    for p in prime:
        if p != 0:
            cnt += 1
    print(cnt)

solve()