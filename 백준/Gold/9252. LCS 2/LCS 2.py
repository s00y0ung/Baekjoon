import sys
input = sys.stdin.readline

def main():
    s1 = list(input().strip())
    s2 = list(input().strip())

    d = [['' for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s2[i-1] == s1[j-1]:
                d[i][j] = d[i-1][j-1]+s2[i-1]
            else:
                if len(d[i-1][j]) > len(d[i][j-1]):
                    d[i][j] = d[i-1][j]
                else:
                    d[i][j] = d[i][j-1]

    print(len(d[-1][-1]))
    if len(d[-1][-1]) != 0:
        print(d[-1][-1])

if __name__ == '__main__':
    main()