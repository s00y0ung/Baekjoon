import sys
input = sys.stdin.readline

def main():
    N = int(input())
    num = list(map(int, input().split()))
    stack = [0]
    neg = [-1]*N

    for i in range(1,N):
        while stack and num[stack[-1]] < num[i]:
            neg[stack.pop()] = num[i]
        stack.append(i)
    print(' '.join(map(str, neg)))

if __name__ == '__main__':
    main()
