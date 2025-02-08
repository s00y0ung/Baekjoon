N = int(input())
cnt = 0
i = 0

while cnt != N:
    i += 1  
    if str(i).count('666') >= 1:
        cnt += 1
print(i)