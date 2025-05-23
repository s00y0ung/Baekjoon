import sys
input = sys.stdin.readline 
def backTracking(arr,start,N,S):
    global result

    for i in range(start,N):
        ans.append(arr[i])
        if sum(ans) == S:
            result += 1
        backTracking(arr, i+1, N, S)
        ans.pop(-1)

N, S = map(int, input().split())
arr = list(map(int, input().split()))

ans = []
result = 0
backTracking(arr, 0, N, S)
print(result)