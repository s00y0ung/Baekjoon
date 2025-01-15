k = int(input())
weight = k
w_list = []

for i in range(2, int(k**0.5)+1):
    while weight % i == 0:
        w_list.append(i)
        weight = weight / i

if weight != 1:
    w_list.append(int(weight))
print(len(w_list))
for w in w_list:
    print(w, end = " ")