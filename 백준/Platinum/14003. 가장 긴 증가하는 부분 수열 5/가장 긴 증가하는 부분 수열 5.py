import sys
input = sys.stdin.readline

def binary_search(a, lis):
    left = 0
    right = len(lis)

    while left < right:
        mid = (left + right)//2
        if lis[mid] < a:
            left = mid + 1
        else:
            right = mid
    return right

N = int(input())
a_list = list(map(int, input().split()))
lis = [a_list[0]]
ans = [0 for i in range(N)]
idx = 0
for a in a_list[1:]:
    idx += 1
    if a > lis[-1]:
        lis.append(a)
        ans[idx] = len(lis)-1
    else:
        b = binary_search(a, lis)
        lis[b] = a
        ans[idx] = b

s = len(lis) - 1
s_list = []
for idx in range(N-1,-1,-1):
    if ans[idx] == s:
        s_list.append(a_list[idx])
        s -= 1

print(len(lis))
print(*s_list[::-1])