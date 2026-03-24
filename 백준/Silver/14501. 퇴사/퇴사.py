import sys
input = sys.stdin.readline

def main():
    n = int(input())
    c = [[] for _ in range(n)]
    for i in range(n):
        a,b = map(int, input().split())
        c[i] = [a,b]

    money = [0 for _ in range(n+1)]
    for i in range(n-1,-1,-1):
        if c[i][0] + i > n:
            money[i] = money[i+1]
            continue
        money[i] = max(c[i][1] + money[i+c[i][0]], money[i+1])
    print(max(money))

if __name__ == '__main__':
    main()