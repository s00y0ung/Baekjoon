import sys

def main():
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    NEG = [-1] * N
    stack = []

    stack.append(0)
    for i in range(1, N):
        while stack and arr[stack[-1]] < arr[i]:
            NEG[stack.pop()] = arr[i]
        stack.append(i)

    print(' '.join(map(str, NEG)))


if __name__ == '__main__':
    main()