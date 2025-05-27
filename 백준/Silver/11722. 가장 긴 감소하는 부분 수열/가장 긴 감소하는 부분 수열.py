def bs(a, lis):
    left = 0
    right = len(lis)

    while left < right:
        mid = (left + right) // 2
        if a < lis[mid]:
            left = mid+1
        elif a > lis[mid]:
            right = mid
        else:
            return mid
    return right

N = int(input())
arr = list(map(int, input().split()))

lis = [arr[0]]
for a in arr[1:]:
    if lis[-1] > a:
        lis.append(a)
        continue
    b = bs(a, lis)
    lis[b] = a

print(len(lis))