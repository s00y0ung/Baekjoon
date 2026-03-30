import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    prime = [0]*1001
    prime[1] = 1
    for i in range(2,1001):
        if prime[i] == 0:
            for j in range(i+i,1001,i):
                prime[j] = 1

    ans = 0
    for c in a:
        if prime[c] == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()