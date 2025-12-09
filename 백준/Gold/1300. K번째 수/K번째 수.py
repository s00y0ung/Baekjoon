import sys
input = sys.stdin.readline

def main():
    N = int(input())
    K = int(input())

    start, end = 1, K
    answer = 0
    while start <= end:
        num = 0
        mid = (start+end) // 2

        for i in range(1,N+1):
            num += min(mid//i, N)

        if num >= K:
            end = mid-1
            answer = mid
        else:
            start = mid+1
    print(answer)

if __name__ == '__main__':
    main()