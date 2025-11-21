import sys
input = sys.stdin.readline
def main():
    n = int(input())
    stack = []
    j = 1
    ans = []
    for i in range(n):
        num = int(input())
        if stack and stack[-1] > num:
            ans = ['NO']
            break

        while not stack or stack[-1] != num:
            stack.append(j)
            j += 1
            ans.append('+')
        stack.pop(-1)
        ans.append('-')
    print('\n'.join(ans))
    
if __name__ == '__main__':
    main()