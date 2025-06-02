def binary_search(c, boxes):
    left = 0
    right = len(boxes)-1

    while left <= right:
        mid = (left+right) // 2

        if boxes[mid] > c:
            right = mid-1
        elif boxes[mid] < c:
            left = mid+1
        else:
            return mid

    return right

N = int(input())
crane = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))
boxes.sort()

crane = [x for x in crane if x >= boxes[0]]
crane = sorted(crane, reverse = True)

ans = 0
if len(crane) == 0:
    ans = -1
elif crane[0] < boxes[-1]: #옮길 수 없는 박스가 존재하는 경우
    ans = -1
else:
    while M > 0:
        if crane[-1] >= boxes[-1]:
            ans += (M // len(crane))
            if M % len(crane) != 0:
                ans += 1
            break

        for c in crane:
            idx = binary_search(c, boxes)
            if idx >= 0:
                M -= 1
                boxes.pop(idx)
        ans += 1

print(ans)