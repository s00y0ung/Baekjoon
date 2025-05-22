def binary_search(N, L, W, H):
    left = 0
    right = 1000000000

    ans = 0
    for _ in range(100):
        mid = (left + right) / 2
        tmp = (L // mid) * (W // mid) * (H // mid)
        if tmp < N:
            right = mid
        else:
            ans = mid
            left = mid
    return ans

N, L, W, H = map(int, input().split())
length = binary_search(N, L, W, H)
print(length)