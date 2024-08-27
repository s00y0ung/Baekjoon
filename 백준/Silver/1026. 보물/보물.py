num = int(input())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list = sorted(a_list, reverse=True) # a_list reverse sorting
a_new_list = a_list.copy()
b_idx = sorted(range(num), key=lambda k : b_list[k]) # index sorting

# a_list relocation
for i in range(num):
    a_new_list[b_idx[i]] = a_list[i]
a_list = a_new_list[:]

s = 0
for i in range(num):
    s += a_list[i] * b_list[i]
    
print(s)