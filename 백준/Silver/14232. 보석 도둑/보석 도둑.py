k = int(input())
weight = k
w_list = []

while weight % 2 == 0:
    w_list.append(2)
    weight = weight / 2
    
for i in range(3, int(k**0.5)+1,2):
    while weight % i == 0:
        w_list.append(i)
        weight = weight / i

if weight != 1:
    w_list.append(int(weight))
print(len(w_list))
print(*w_list)