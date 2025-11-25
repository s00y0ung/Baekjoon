import sys
input = sys.stdin.readline

def main():
    N,K = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    print(arr[K-1])
if __name__ == '__main__':
    main()