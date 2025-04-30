def hanoi_top(N, to, tmp, fm):
    if N == 1:
        print(to,fm)
        return
    hanoi_top(N - 1, to, fm, tmp)
    hanoi_top(1, to, tmp, fm)
    hanoi_top(N - 1, tmp, to, fm)

N = int(input())
print(2**N-1)
hanoi_top(N,1,2,3)