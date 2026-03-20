import sys
import math
input = sys.stdin.readline

def main():
    n,m,k = map(int, input().split())
    tree_n = math.ceil(math.log(n,2))
    tree = [1 for _ in range(2**(tree_n+1))]
    for i in range(2**tree_n, 2**tree_n+n):
        tree[i] = int(input())
    for i in range(2**tree_n-1,0,-1):
        tree[i] = tree[2*i]*tree[2*i+1] % 1000000007

    for _ in range(m+k):
        a,b,c = map(int, input().split())
        if a == 1:
            b = 2 ** tree_n + b - 1
            tree[b] = c
            while b//2 > 0:
                b = b//2
                tree[b] = tree[b*2] * tree[b*2+1] % 1000000007
        elif a == 2:
            b,c = 2**tree_n+b-1, 2**tree_n+c-1
            tmp = 1
            while b <= c:
                if b%2 == 1:
                    tmp = tree[b] * tmp % 1000000007
                if c%2 == 0:
                    tmp = tree[c] * tmp % 1000000007
                b = (b+1)//2
                c = (c-1)//2
            print(tmp)

if __name__ == '__main__':
    main()