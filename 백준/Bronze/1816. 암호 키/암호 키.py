m = int(input())
for i in range(m):
    n = int(input())
    flag = 'YES'
    for j in range(2,min(n, 10**6)):
        if n % j == 0:
            flag = 'NO'
            break
    print(flag)