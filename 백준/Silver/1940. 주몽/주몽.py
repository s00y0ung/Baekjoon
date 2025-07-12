N = int(input())
M = int(input())
nums = list(map(int, input().split()))
nums.sort()

ans = 0
s,e = 0,N-1
while s < e:
    t = nums[s] + nums[e]
    if t > M:
        e -= 1
    elif t < M:
        s += 1
    else:
        ans += 1
        e -= 1
        s += 1
print(ans)