N = int(input())
prime = []
num = N

i = 2
while i < N or num == 0:
    if num % i == 0:
        prime.append(i)
        num = num / i
    else:
        i += 1

if len(prime) == 0:
    if N != 1:
        prime.append(N)

for p in prime:
    print(p)