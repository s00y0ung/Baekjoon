import sys
input = sys.stdin.readline

def main():
    N = int(input())
    arr = [0]*10001
    for i in range(N):
        a = int(input())
        arr[a] += 1
    
    for i in range(10001):
        for j in range(arr[i]):
            print(i)

if __name__ == '__main__':
    main()