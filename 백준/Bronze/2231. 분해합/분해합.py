N = int(input())
flag = 0

for n in range(1000000):
    num = 0
    tmp = n
    while tmp > 0:
        num += (tmp%10)
        tmp = tmp//10
        
    num = num + tmp + n

    if N == num:
        print(n)
        flag = 1
        break
if flag == 0:
    print(0)