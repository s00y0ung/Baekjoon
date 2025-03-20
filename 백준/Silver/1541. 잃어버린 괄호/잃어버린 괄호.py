num_list = list(input().split('-'))

for n in range(len(num_list)):
    if '+' in num_list[n]:
        p_list = list(num_list[n].split('+'))
        p = 0
        for pNum in p_list:
            p += int(pNum)
        num_list[n] = p
    else:
        num_list[n] = int(num_list[n])

ans = num_list[0]
for i in range(1, len(num_list)):
    ans -= num_list[i]
print(ans)