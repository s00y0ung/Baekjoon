import sys
import math
input = sys.stdin.readline

def main():
    a,b = map(int, input().split())
    tmp = int(b//a)
    ans = [0,0]
    result = 1e9
    for cnt in range(1, int(tmp**0.5)+1):
        if tmp % cnt == 0 and math.gcd(cnt, tmp//cnt) == 1:
            if result > cnt*a+(tmp//cnt)*a:
                ans = [cnt, tmp//cnt]
    print(ans[0]*a, ans[1]*a)

if __name__ == '__main__':
    main()