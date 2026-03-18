import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    s = set()
    ans = 0
    for _ in range(n):
        s.add(input().strip())

    for _ in range(m):
        tmp = input().strip()
        if tmp in s:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()