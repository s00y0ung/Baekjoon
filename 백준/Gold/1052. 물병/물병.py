N, K = map(int, input().split())
n_list =list(str(format(N, 'b')).rjust(25,'0'))

cnt = n_list.count('1')
ans = -1
if K >= cnt:
    ans = 0
else:
    v = []
    value = 0
    for i in range(24,-1,-1):
        if n_list[i] == '1':
            v.append(i)
            value = i
            continue
        if cnt-len(v) < K:
            for j in range(len(v)):
                n_list[v[j]] = '0'
            n_list[value-1] = '1'
            break
    ans = int('0b'+''.join(n_list),2) - N
print(ans)