t_list = list(map(int, input().split()))
t_list.sort()

if t_list[2] < t_list[1]+t_list[0]:
    print(sum(t_list))
else:
    print(2*(t_list[0]+t_list[1])-1)