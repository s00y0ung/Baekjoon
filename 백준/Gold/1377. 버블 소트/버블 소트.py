import sys
input = sys.stdin.readline

def main():
    N = int(input())
    arr = []
    for i in range(N):
        arr.append((int(input()),i))
    arr.sort(key = lambda x:x[0])

    ans = 0
    for i in range(N):
        if ans < arr[i][1]-i:
            ans = arr[i][1]-i

    print(ans+1)

if __name__ == '__main__':
    main()