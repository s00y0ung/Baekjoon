def solve():
    A, B = map(int, input().split())

    while B != 0:
        A, B = B, A%B

    for i in range(A):
        print(1,end="")

solve()