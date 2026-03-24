import sys
input = sys.stdin.readline

def main():
    n = int(input())
    d = [0,0,1,1]

    for i in range(4,n+1):
        t1,t2 = 1000000,1000000
        if i%3 == 0:
            t1 = d[i//3]
        if i%2 == 0:
            t2 = d[i//2]
        d.append(min(t1,t2,d[i-1])+1)
    print(d[n])

if __name__ == '__main__':
    main()