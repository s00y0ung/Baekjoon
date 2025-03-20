num_list = input().split('-')
ans = []

for n in num_list:
    cnt = 0
    s = n.split('+')
    for j in s:
        cnt += int(j)
    ans.append(cnt)

n = ans[0]
for i in range(1, len(ans)):
    n -= ans[i]
print(n)