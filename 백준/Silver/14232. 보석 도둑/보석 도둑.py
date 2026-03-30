import sys
input = sys.stdin.readline

def main():
    N = int(input())
    ans = []
    for i in range(2, int(N**0.5)+1):
        if N % i != 0:
            continue

        while N % i == 0:
            N //= i
            ans.append(i)
    if N != 1:
        ans.append(N)
    print(len(ans))
    print(*ans)
if __name__ == '__main__':
    main()