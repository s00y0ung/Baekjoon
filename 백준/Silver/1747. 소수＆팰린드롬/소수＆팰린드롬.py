import sys
input = sys.stdin.readline

def main():
    N = int(input())
    if N >= 100000:
        print(1003001)
    else:
        prime = [1] * 100000
        prime[1] = 0
        for i in range(2,100000):
            if prime[i] == 1:
                if i >= N and str(i) == str(i)[::-1]:
                    print(i)
                    break
                for j in range(i+i,100000,i):
                    prime[j] = 0

if __name__ == '__main__':
    main()