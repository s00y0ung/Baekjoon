import sys
input = sys.stdin.readline

def main():
    N = int(input())
    ans = 1
    total = 3
    s,e = 1,2
    if N == 1 or N == 2:
        print(1)
    else:
        while s <= e <= (N // 2 + 1):
            if total == N:
                ans += 1
                total -= s
                s += 1
            elif total > N:
                total -= s
                s += 1
            elif total < N:
                e += 1
                total += e

        print(ans)
main()