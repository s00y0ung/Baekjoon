import sys
input = sys.stdin.readline

def binary_search(check, arr):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == check:
            return 1
        elif arr[mid] < check:
            low = mid+1
        else:
            high = mid-1
    return 0

def main():
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    check = list(map(int, input().split()))

    arr.sort()
    for i in range(M):
        print(binary_search(check[i],arr))

if __name__ == "__main__":
    main()