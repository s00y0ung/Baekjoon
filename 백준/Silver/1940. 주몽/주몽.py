N = int(input())
M = int(input())
weapon = list(map(int, input().split()))

weapon = sorted(weapon)
s = 0
e = len(weapon)-1
ans = 0
while s < e:
    if weapon[s]+weapon[e] == M:
        ans += 1
        s += 1
        e -= 1
    elif weapon[s] + weapon[e] > M:
        e -= 1
    else:
        s += 1
print(ans)