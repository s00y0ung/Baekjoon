N = int(input())
prime = list(map(int, input().split()))
count = 0

for p in prime:
    flag = 0
    if p == 1:
        continue
        
    for i in range(2, p): 
        if p % i == 0:
            flag = 1
            break
    if flag == 0:
        count += 1
print(count)