import sys
input = sys.stdin.readline

def binary_search(d,s,e,p,target):
    if p == e:
        e -= 1
    if p == s:
        s += 1
    while s < e:
        if d[s]+d[e] == target:
            return 1
        elif d[s]+d[e] > target:
            e -= 1
            if p == e:
                e -= 1
        else:
            s += 1
            if p == s:
                s += 1

    return 0

N = int(input())
d = list(map(int, input().split()))
d.sort()
ans = 0
for c in range(N):
    ans += binary_search(d,0,N-1,c,d[c])

print(ans)