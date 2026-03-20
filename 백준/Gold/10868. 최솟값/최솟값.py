import sys
import math
input = sys.stdin.readline
INF = int(1e9)

def main():
    n,m = map(int, input().split())
    tree_n = math.ceil(math.log(n,2))
    tree = [INF for _ in range(2**(tree_n+1))]
    for i in range(2**tree_n, 2**tree_n+n):
        tree[i] = int(input())
    for i in range(2**tree_n-1,0,-1):
        tree[i] = min(tree[2*i],tree[2*i+1])

    for _ in range(m):
        a,b = map(int, input().split())
        a,b = 2**tree_n+a-1, 2**tree_n+b-1
        tmp = INF
        while a <= b:
            if a % 2 == 1:
                tmp = min(tmp, tree[a])
            if b % 2 == 0:
                tmp = min(tmp, tree[b])
            a = (a+1)//2
            b = (b-1)//2
        print(tmp)

if __name__ == '__main__':
    main()