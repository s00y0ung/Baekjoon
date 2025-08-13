import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge(left, right):
    i, j = 0,0
    sorted_list = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    leftarr = merge_sort(left)
    rightarr = merge_sort(right)
    return merge(leftarr,rightarr)


N = int(input())
arr = [int(input()) for _ in range(N)]
a_list = merge_sort(arr)
print("\n".join(map(str,a_list)))