import sys
input = sys.stdin.readline

def binary_search(LIS, target, start, end):

    while start < end:
        mid = (start + end) // 2
        if LIS[mid] < target:
            start = mid+1
        else:
            end = mid
    return start

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    LIS = [arr[0]]
    dp = [0 for _ in range(n)]
    dp[0] = 1
    for i in range(1, n):
        if arr[i] > LIS[-1]:
            LIS.append(arr[i])
            dp[i] = len(LIS)
        else:
            s = binary_search(LIS,arr[i],0,len(LIS))
            LIS[s] = arr[i]
            dp[i] = s+1

    max_t = len(LIS)
    print(max_t)
    ans = []
    for c in range(n-1,-1,-1):
        if dp[c] == max_t:
            ans.append(arr[c])
            max_t -= 1
    print(*ans[::-1])

if __name__ == '__main__':
    main()