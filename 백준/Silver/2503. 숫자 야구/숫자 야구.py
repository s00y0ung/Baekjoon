n = int(input())
base = []
for i in range(n):
    base.append(list(map(int, input().split())))

answer = 0
for i in range(123, 988):
    if i%10 == 0 or i//10%10==0:
        continue
    if i%10 == i//100 or i%10 == i//10%10 or i//100 == i//10%10:
        continue

    num = str(i)
    f = 1
    for b, strike, ball in base:
        b = str(b)
        s_cnt = 0
        b_cnt = 0
        if num[0] == b[0]: s_cnt += 1
        elif num[0] in b: b_cnt += 1
        if num[1] == b[1]: s_cnt += 1
        elif num[1] in b: b_cnt += 1
        if num[2] == b[2]: s_cnt += 1
        elif num[2] in b: b_cnt += 1

        if strike != s_cnt or ball != b_cnt:
            f = 0
            break
    if f:
        answer += 1
print(answer)