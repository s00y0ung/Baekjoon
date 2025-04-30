def hanoi_top(N, to, tmp, fm):
    global ans, ans_list
    if N == 1:
        ans += 1
        ans_list.append([to,fm])
        return
    hanoi_top(N - 1, to, fm, tmp)
    hanoi_top(1, to, tmp, fm)
    hanoi_top(N - 1, tmp, to, fm)

N = int(input())
ans = 0
ans_list = []
hanoi_top(N,1,2,3)

print(ans)
for idx in range(ans):
    print(ans_list[idx][0], ans_list[idx][1])