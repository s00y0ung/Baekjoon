import sys
input = sys.stdin.readline

def main():
    arr = list(input().strip())
    arr.sort(reverse = True)
    print(''.join(arr))

if __name__ == '__main__':
    main()