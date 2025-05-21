list = list(map(int, input().split()))

min_num = 1
while True:
    min_num += 1
    a = 1 if min_num % list[0] == 0 else 0
    b = 1 if min_num % list[1] == 0 else 0
    c = 1 if min_num % list[2] == 0 else 0
    d = 1 if min_num % list[3] == 0 else 0
    e = 1 if min_num % list[4] == 0 else 0

    if a+b+c+d+e >= 3:
        print(min_num)
        break