N = int(input())
ans = 0
s,e = 1,1
total = 1
while s <= e <= N:
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
