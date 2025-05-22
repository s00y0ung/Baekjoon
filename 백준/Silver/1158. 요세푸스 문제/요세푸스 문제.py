N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]

t = 0
ans = []
for i in range(N):
    t = (t + K-1) % len(arr)
    ans.append(str(arr[t]))
    arr.pop(t)
print(f"<{', '.join(ans)}>")