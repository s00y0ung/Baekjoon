import sys
import math
input = sys.stdin.readline

def main():
    n = int(input())
    t = list(map(int, input().split()))
    a = [math.factorial(i) for i in range(n - 1, 0, -1)] + [0]
    num_list = [i for i in range(1, n + 1)]

    if t[0] == 1:
        k = t[1]-1
        ans = []
        for i in range(n-1):
            q,r = k // a[i], k%a[i]
            ans.append(num_list[q])
            num_list.pop(q)
            k = r
        print(*(ans + num_list))
    else:
        p = t[1:]
        ans = 1
        for i in range(n):
            idx = num_list.index(p[i])
            ans += idx*a[i]
            num_list.pop(idx)
        print(ans)

if __name__ == '__main__':
    main()