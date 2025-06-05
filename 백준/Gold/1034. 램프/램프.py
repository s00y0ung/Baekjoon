n,m = map(int,input().split())
lst = [input() for _ in range(n)]

k = int(input())
max_cnt = 0

for col in range(n):
    zero_count = 0
    for lc in lst[col]:
        if lc == '0':
            zero_count += 1

    col_cnt = 0
    if zero_count <= k and zero_count%2 == k%2:
        for c in range(n):
            if lst[c] == lst[col]:
                col_cnt += 1
    max_cnt = max(max_cnt, col_cnt)

print(max_cnt)