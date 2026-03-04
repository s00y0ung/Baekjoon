import sys
input = sys.stdin.readline

def main():
    a,b = map(int, input().split())

    prime = [1]*(int(b**0.5)+1)
    prime[1] = 0
    ans = 0
    for i in range(2, int(b**0.5)+1):
        if prime[i] == 1:
            for j in range(i+i, int(b**0.5)+1, i):
                prime[j] = 0

            tmp = i*i
            while  tmp <= b:
                if a <= tmp:
                    ans += 1
                tmp *= i
    print(ans)
if __name__ == "__main__":
    main()