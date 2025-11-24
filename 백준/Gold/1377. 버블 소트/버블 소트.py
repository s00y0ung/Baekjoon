import sys
input = sys.stdin.readline

def main():
    N = int(input())
    arr = [0] * N
    for i in range(N):
        arr[i] = [int(input()),i]
    arr = sorted(arr, key = lambda x:x[0])
    ans = 0
    for i in range(N):
        if ans < (arr[i][1]-i+1):
            ans = (arr[i][1]-i+1)
    print(ans)
if __name__ == '__main__':
    main()