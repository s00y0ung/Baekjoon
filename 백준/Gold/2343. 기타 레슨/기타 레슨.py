import sys
input = sys.stdin.readline

def binary_search(start, end, blu_ray, N, M):
    while start <= end:
        mid = (start+end)//2
        cnt = 0
        total = 0
        for i in range(N):
            total += blu_ray[i]
            if total > mid:
                total = blu_ray[i]
                cnt += 1

        if cnt >= M:
            start = mid+1
        else:
            end = mid-1
    return start, end

def main():
    N,M = map(int, input().split())
    blu_ray = list(map(int, input().split()))

    start,end = binary_search(max(blu_ray), sum(blu_ray), blu_ray, N, M)

    print(start)


if __name__ == '__main__':
    main()
