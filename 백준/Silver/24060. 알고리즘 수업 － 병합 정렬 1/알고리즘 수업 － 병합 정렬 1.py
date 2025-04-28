import sys
input = sys.stdin.readline

def merge_sort(arr, l, mid, r):
    global ans_k

    i = l
    j = mid+1
    tmp = []
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= mid:
        tmp.append(arr[i])
        i += 1

    while j <= r:
        tmp.append(arr[j])
        j += 1

    t = 0
    for idx in range(l, r+1):
        ans_k.append(tmp[t])
        arr[idx] = tmp[t]
        t += 1

def partition(arr, l, r):
    if l < r:
        mid = (l+r)//2
        partition(arr, l, mid)
        partition(arr, mid+1, r)
        merge_sort(arr, l, mid, r)

A,K = map(int, input().split())
arr = list(map(int, input().split()))

ans_k = []
partition(arr, 0, len(arr)-1)
print(-1 if len(ans_k) <= K else ans_k[K-1])
