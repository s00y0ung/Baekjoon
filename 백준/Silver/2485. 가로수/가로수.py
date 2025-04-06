import sys
input = sys.stdin.readline

def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a

N = int(input())

diff_list = []

pre = int(input())
next = int(input())
diff_list.append(next - pre)

pre = next
next = int(input())
diff_list.append(next-pre)

g = gcd(diff_list[0], diff_list[1])
pre = next

for _ in range(N-3):
    next = int(input())
    diff_list.append(next-pre)
    g = gcd(g, next-pre)
    pre = next

ans = 0
for d in diff_list:
    ans += (d//g - 1)
print(ans)
