import sys

def main():
    n = int(input())
    li = list(map(int, sys.stdin.read().split()))
    li.sort()
    for x in li:
        sys.stdout.write(str(x) + '\n')
    
if __name__ == '__main__':
    main()