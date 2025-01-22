N, B = map(int, input().split())

n = ""
while N != 0:
    remain = N % B
    N = N // B

    if remain >= 10:
        remain = chr(remain+55)
    
    n = f'{remain}{n}'


print(n)