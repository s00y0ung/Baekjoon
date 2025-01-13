N = int(input())

b_list = list(map(int, input().split()))
p_list = [0 for i in range(N)]

for i in range(N):
    min_el = 1001
    min_idx = -1
    
    for j in range(N):
        if min_el > b_list[j]:
            min_idx = j
            min_el = b_list[j]
    b_list[min_idx] = 1001    
    p_list[min_idx] = i

for i in range(N):
    print(p_list[i], end = " ")