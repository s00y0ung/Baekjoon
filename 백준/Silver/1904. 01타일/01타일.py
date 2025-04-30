N = int(input())
p = 1
pp = 1
cur = 1
for idx in range(2,N+1):
    cur = (p+pp)%15746
    pp = p
    p = cur
print(cur%15746)