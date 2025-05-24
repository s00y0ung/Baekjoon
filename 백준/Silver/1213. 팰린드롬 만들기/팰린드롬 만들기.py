name = input().rstrip()
name_dic = {}

name = sorted(name)
for n in name:
    if n in name_dic:
        name_dic[n] += 1
    else:
        name_dic[n] = 1

flag = 0
odd = '-'
front = []
rear = []

tmp = 0
for n_key, n_value in name_dic.items():
    if n_value % 2 == 1:
        if flag == 2:
            ans = -1
            break
        flag += 1
        odd = n_key

    for i in range(n_value//2):
        front.append(n_key)
        rear.append(n_key)
if flag == 1:
    ans = front + [odd] + rear[::-1]
elif flag == 2:
    ans = ["I'm Sorry Hansoo"]
else:
    ans = front + rear[::-1]

print(''.join(ans))