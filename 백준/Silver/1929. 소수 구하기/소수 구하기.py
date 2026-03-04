import sys
input = sys.stdin.readline

def main():
    M, N = map(int, input().split())

    prime = [1]*(N+1)
    prime[1] = 0
    for i in range(2, int(N**0.5)+1):
        if prime[i] == 1:
            for j in range(i+i,N+1,i):
                prime[j] = 0

    for i in range(M, N+1):
        if prime[i]:
            print(i)

if __name__ == "__main__":
    main()