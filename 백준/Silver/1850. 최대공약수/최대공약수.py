import sys
input = sys.stdin.readline

def main():
    a,b = map(int, input().split())
    while b > 0:
        a,b = b, a%b
    print('1'*a)

if __name__ == '__main__':
    main()