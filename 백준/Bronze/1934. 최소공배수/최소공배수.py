import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        a,b = map(int, input().split())
        tmp = a*b
        while b > 0:
            a,b = b,a%b
        print(tmp//a)
        
if __name__ == '__main__':
    main()