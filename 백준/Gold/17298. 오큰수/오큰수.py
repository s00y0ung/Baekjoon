import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
que = []
ans = [-1 for _ in range(N)]
for i in range(N):
    while que and que[-1][1] < arr[i]:
        ans[que[-1][0]] = arr[i]
        que.pop()
    que.append([i, arr[i]])
print(*ans)