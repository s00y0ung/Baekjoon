import sys
import math
input = sys.stdin.readline

def main():
    test = int(input())
    for _ in range(test):
        n,m = map(int, input().split())
        print(math.factorial(m)//(math.factorial(m-n)*math.factorial(n)))

if __name__ == '__main__':
    main()