import sys
input = sys.stdin.readline

def main():
    N = int(input())
    time = []
    for _ in range(N):
        time.append(list(map(int, input().split())))
    time = sorted(time, key = lambda x : (x[1],x[0]))

    ans = 0
    p_end = 0
    for start, end in time:
        if start >= p_end:
            ans += 1
            p_end = end
    print(ans)

if __name__ == "__main__":
    main()