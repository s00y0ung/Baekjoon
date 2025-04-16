import sys
input = sys.stdin.readline

def get_p(n, n_list, total):

    s = len(n_list)

    for _ in range(N-1):
        total = total // s
        quo = n // total
        rem = n % total
        print(n_list[quo], end = " ")
        n_list.pop(quo)

        s -= 1
        n = rem
    print(n_list[0])

def get_o(k_list, total):
    ans = 0
    s = len(k_list)

    for idx in k_list[:-1]:
        total = total // s
        s = s-1
        ans = ans + total * n_list.index(idx)
        n_list.remove(idx)

    print(ans+1)


N = int(input())
n_list = [i for i in range(1,N+1)]
K_list = list(map(int, input().split()))

total = 1
for idx in range(1, N+1):
    total = total * idx

if K_list[0] == 1:
    get_p(K_list[1]-1, n_list, total)
else: # K[0] == 2
    get_o(K_list[1:], total)
