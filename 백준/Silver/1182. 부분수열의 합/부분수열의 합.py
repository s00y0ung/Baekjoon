def backTracking(arr,start,N,S):
    global result
    if sum(ans) == S and len(ans) > 0:
        result += 1

    for i in range(start,N):
        ans.append(arr[i])
        backTracking(arr, i+1, N, S)
        ans.pop(-1)

N, S = map(int, input().split())
arr = list(map(int, input().split()))

ans = []
result = 0
backTracking(arr, 0, N, S)
print(result)