import sys
input = sys.stdin.readline

def main():
    n = int(input())
    d = [0,1,2] + [0]*n

    for i in range(3,n+1):
        d[i] = (d[i-1]+d[i-2])%10007
    print(d[n])

if __name__ == '__main__':
    main()