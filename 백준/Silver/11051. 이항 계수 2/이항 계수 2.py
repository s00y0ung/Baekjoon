import sys
import math
input = sys.stdin.readline

def main():
    n,k = map(int, input().split())
    print(math.factorial(n)//(math.factorial(k) * math.factorial(n-k)) %10007)

if __name__ == '__main__':
    main()