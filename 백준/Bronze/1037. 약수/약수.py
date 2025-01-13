N = int(input())
a_list = list(map(int, input().split()))

a_list.sort()
if len(a_list) == 1:
    print(a_list[0] ** 2)
else:
    print(a_list[0] * a_list[len(a_list)-1])