import sys
input = sys.stdin.readline

def main():
    N = int(input())
    M = int(input())

    start = 1
    end = M
    ans = 0

    while start <= end:
        mid = (start+end)//2
        cnt = 0
        for i in range(1,N+1):
            cnt += min(mid//i, N)
        if cnt >= M:
            ans = mid
            end = mid-1
        else:
            start = mid+1
    print(ans)

if __name__ == "__main__":
    main()