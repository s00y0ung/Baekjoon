A,B = map(int, input().split())

prime = [i for i in range(B+1)]
under_prime = [0 for _ in range(B+1)]
ans = 0
prime[1] = 1
for i in range(2,B+1):
    if prime[i] == 0:
        continue
    prime[i] = 1
    for j in range(i+i,B+1,i):
        prime[j] = 0


for i in range(2,B+1):
    if prime[i] == 1:
        under_prime[i] = 1
        continue

    for j in range(2, i):
        if i % j == 0:
            under_prime[i] = under_prime[j] + under_prime[i//j]
            if A <= i <=B and prime[under_prime[i]] == 1:
                ans += 1
            break
print(ans)