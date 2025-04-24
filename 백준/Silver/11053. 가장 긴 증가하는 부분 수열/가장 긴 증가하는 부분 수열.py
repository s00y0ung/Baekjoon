import sys
input = sys.stdin.readline

def binary_search(a, lis):
    left = 0
    right = len(lis)
    while left < right:
        mid = (left + right) // 2
        if lis[mid] > a:
            right = mid
        elif lis[mid] < a:
            left = mid+1
        else:
            return mid
    return right


N = int(input())
a_list = list(map(int, input().split()))
lis = [a_list[0]]

for a in a_list[1:]:
    b = binary_search(a, lis)

    if b > len(lis)-1:
        lis.append(a)
    else:
        lis[b] = a

print(len(lis))