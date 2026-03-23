import sys
input = sys.stdin.readline

def main():
    n = int(input())
    d = [0,0,1]
    for i in range(3,n+1):
        d.append((i-1)*(d[i-1]+d[i-2])%1000000000)
    print(d[n])

if __name__ == '__main__':
    main()