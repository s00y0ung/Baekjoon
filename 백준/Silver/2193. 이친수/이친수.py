import sys
input = sys.stdin.readline

def main():
    n = int(input())
    d = [[0,0],[0,1],[1,0]]

    for i in range(3,n+1):
        d.append([d[i-1][0]+d[i-1][1], d[i-1][0]])
    print(sum(d[n]))
    
if __name__ == '__main__':
    main()