import sys
input = sys.stdin.readline

def main():
    n = int(input())
    csod = 0
    for i in range(2, int(n**0.5)+1):
        k = n//i
        csod += (k*(k+1)//2 - i*(i+1)//2 + i*(k-i)+i)
        csod = csod%1000000

    print(csod)

if __name__ == '__main__':
    main()