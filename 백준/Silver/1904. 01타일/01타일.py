N = int(input())
p = 1
pp = 1
for idx in range(2,N+1):
    pp,p = p,(p+pp)%15746

print(p)