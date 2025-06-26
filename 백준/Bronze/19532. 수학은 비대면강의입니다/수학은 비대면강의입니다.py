a,b,c,d,e,f = map(int, input().split())
flag = 0
for i in range(-999,1000):
    for j in range(-999,1000):
        if a*i + b*j != c:
            continue
        if d*i + e*j != f:
            continue
        flag = 1
        print(i, j)
        break
    if flag:
        break