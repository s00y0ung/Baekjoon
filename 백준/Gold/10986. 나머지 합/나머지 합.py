import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = list(map(int, input().split()))

prefix = [0]
div = [0 for i in range(m)]
for i in range(n):
    prefix.append(prefix[-1]+nums[i])
    div[prefix[-1]%m] += 1

ans = div[0]
for i in range(m):
    a = div[i]
    ans += (a*(a-1)//2)
print(ans)