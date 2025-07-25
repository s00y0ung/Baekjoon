n = int(input())

if n == 1 or n == 2:
    print(n)
else:
    k = 1
    while 2**k < n:
        k += 1
    print(2**k - (2**k - n)*2)