import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    L = [0 for _ in range(n)]
    R = [0 for _ in range(n)]
    ans = arr[0]
    
    L[0] = arr[0]
    for i in range(1,n):
        L[i] = max(L[i-1] + arr[i], arr[i])
        ans = max(ans, L[i])
    R[-1] = arr[-1]
    for i in range(n-2,-1,-1):
        R[i] = max(R[i+1]+arr[i], arr[i])
    
    for i in range(1,n-1):
        ans = max(L[i-1]+R[i+1],ans)
    print(ans)

if __name__ == '__main__':
    main()