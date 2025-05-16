L,R = input().split()
L = list(L)
R = list(R)

ans = 0
if len(L) == len(R):
    for i in range(len(R)):
        if L[i] == R[i]:
            if L[i] == '8':
                ans += 1
        else:
            break
print(ans)