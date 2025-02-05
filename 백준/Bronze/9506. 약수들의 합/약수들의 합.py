def get_divisor(n):
    divisor_list = []
    for i in range(1,n):
        if n % i == 0:
            divisor_list.append(i)
    return divisor_list

n = int(input())
while(n != -1):
    divisor_list = get_divisor(n)
    if n == sum(divisor_list):
        print(f"{n} = ", end ="")
        for num in divisor_list[:len(divisor_list)-1]:
            print(f"{num} + ", end="")
        print(f"{divisor_list[-1]}")
        
    else:
        print(f"{n} is NOT perfect.")
    n = int(input())