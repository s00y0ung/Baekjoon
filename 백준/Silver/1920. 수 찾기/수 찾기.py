def binary_search(search):
    global N_list, N

    left = 0
    right = N-1

    while left <= right:
        mid = (left + right)//2
        if N_list[mid] > search:
            right = mid-1
        elif N_list[mid] < search:
            left = mid+1
        else:
            return 1

    return 0



if __name__ == "__main__":
    N = int(input())
    N_list = list(map(int, input().split()))
    N_list.sort()

    M = int(input())
    M_list = list(map(int, input().split()))

    for m in M_list:
        print(binary_search(m))