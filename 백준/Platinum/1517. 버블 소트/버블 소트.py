import sys
swap = 0

def merge(left, right):
    i,j = 0,0
    sorted_list = []
    global swap

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
            swap = swap + len(left)-i

    if i < len(left):
        sorted_list.extend(left[i:])
    else:
        sorted_list.extend(right[j:])
    return sorted_list

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
merge_sort(arr)
print(swap)