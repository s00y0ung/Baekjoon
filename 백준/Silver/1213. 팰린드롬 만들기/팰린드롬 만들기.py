name = input().rstrip()
name_list = [0 for i in range(26)]

for n in name:
    name_list[ord(n)-65] += 1

flag = 0
odd = '-'
front = []
tmp = 0
for idx in range(26):
    if name_list[idx] == 0:
        continue

    if name_list[idx] % 2 == 1:
        if flag == 2:
            break
        flag += 1
        odd = chr(idx+65)

    for i in range(name_list[idx]//2):
        front.append(chr(idx+65))
        
if flag == 1:
    ans = front + [odd] + front[::-1]
elif flag == 2:
    ans = ["I'm Sorry Hansoo"]
else:
    ans = front + front[::-1]

print(''.join(ans))