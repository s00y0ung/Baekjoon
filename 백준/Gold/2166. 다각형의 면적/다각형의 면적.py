import sys
input = sys.stdin.readline

def main():
    n = int(input())
    ans = 0
    point = []
    for _ in range(n):
        point.append(list(map(int, input().split())))
    point.append(point[0])
    for i in range(n):
        ans = ans + point[i][0]*point[i+1][1] - point[i+1][0]*point[i][1]
    print(abs(ans)/2)

if __name__ == '__main__':
    main()