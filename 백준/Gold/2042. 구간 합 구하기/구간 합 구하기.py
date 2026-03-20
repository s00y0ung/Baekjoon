import sys
import math
input = sys.stdin.readline

def main():
    n,m,k = map(int, input().split())
    tree_n = math.ceil(math.log(n,2))
    tree = [0 for _ in range(2**(tree_n+1))]
    for i in range(2**tree_n,2**tree_n+n):
        tree[i] = int(input())
    for i in range(2**tree_n-1,0,-1):
        tree[i] = tree[i*2]+tree[i*2+1]

    for i in range(m+k):
        a,b,c = map(int, input().split())
        if a == 1:
            b = 2**tree_n+b-1
            tmp = c - tree[b]
            tree[b] = c
            while b//2 > 0:
                tree[b//2] += tmp
                b = b//2
        else:
            b,c = 2**tree_n+b-1, 2**tree_n+c-1
            tmp = 0
            while b <= c:
                if b % 2 == 1:
                    tmp += tree[b]
                if c % 2 == 0:
                    tmp += tree[c]
                b = (b+1)//2
                c = (c-1)//2
            print(tmp)

if __name__ == '__main__':
    main()