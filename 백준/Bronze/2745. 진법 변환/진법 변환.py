N, B = input().split()
B = int(B)


sum = 0;
for i in range(len(N)):
    num = ord(N[len(N)-i-1])
    if num >= 65: #A
        sum += (num-55) * (B**i)
    else:
        sum += (num-48) * (B**i)
print(sum)

