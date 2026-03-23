import sys
import math
input = sys.stdin.readline

def main():
    m = int(input())
    color = list(map(int, input().split()))
    total = sum(color)
    k = int(input())

    tmp = 0
    for c in color:
        if c >= k:
            tmp += (math.factorial(c) // (math.factorial(c-k)*math.factorial(k)))
    print(tmp / (math.factorial(total) // (math.factorial(total-k)*math.factorial(k))))
if __name__ == '__main__':
    main()