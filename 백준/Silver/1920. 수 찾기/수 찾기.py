N = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

M = int(input())
m_list = list(map(int, input().split()))

for m in m_list:
    left = 0
    right = N-1
    flag = 1
    
    while left <= right:
        mid = (left + right)//2
        if n_list[mid] == m:
            flag = 0
            break

        if n_list[mid] > m:
            right = mid-1
        else:
            left = mid+1
            
    if flag == 1:
        print(0)
    else:
        print(1)