N = int(input())

for i in range(N):
    C = int(input())
    change_list = []

    change_list.append(C // 25)
    C = C%25

    change_list.append(C // 10)
    C = C%10

    change_list.append(C // 5)
    C = C%5

    change_list.append(C)

    print(*change_list)

    