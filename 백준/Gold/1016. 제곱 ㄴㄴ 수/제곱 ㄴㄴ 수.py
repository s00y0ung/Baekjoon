import sys
input = sys.stdin.readline

def main():
    MIN, MAX = map(int, input().split())
    prime = [1 for i in range(MIN, MAX + 1)]

    for i in range(2, int(MAX ** 0.5) + 1):
        s = i * i
        s_idx = (MIN // s) * s
        for j in range(s_idx, MAX + 1, i * i):
            if j >= MIN:
                prime[j - MIN] = 0

    print(sum(prime))

if __name__ == '__main__':
    main()