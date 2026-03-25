import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(input().strip()))

    ans = 0
    d = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1, m+1):
            if arr[i-1][j-1] == '0':
                d[i][j] = 0
            elif d[i][j-1] == 0 or d[i-1][j] == 0 or d[i-1][j-1] == 0:
                d[i][j] = int(arr[i-1][j-1])
            elif d[i][j-1] == d[i-1][j] == d[i-1][j-1]:
                d[i][j] = d[i-1][j-1] + 1
            else:
                d[i][j] = min(d[i][j-1],d[i-1][j],d[i-1][j-1])+1
        ans = max(ans, max(d[i]))
    print(ans*ans)
if __name__ == '__main__':
    main()