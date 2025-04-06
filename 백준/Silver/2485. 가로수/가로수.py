def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a

N = int(input())

diff_list = []

pre = int(input())
for _ in range(N-1):
    next = int(input())
    diff_list.append(next-pre)
    pre = next

g = gcd(diff_list[0], diff_list[1])
for d in range(2,N-1):
    g = gcd(diff_list[d], g)

ans = 0
for d in diff_list:
    ans += (d//g - 1)
print(ans)
