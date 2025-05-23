def backTracking(idx, result):
    global ans, arr, N, S
    if idx == N:
        if result == S:
            ans += 1
        return

    backTracking(idx+1, result)
    backTracking(idx+1, result+arr[idx])


N, S = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
backTracking(0, 0)
if S == 0:
    ans -= 1
print(ans)