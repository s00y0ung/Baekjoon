import sys
input = sys.stdin.readline

def main():
    N = int(input())
    conference = []
    for _ in range(N):
        start, end = map(int, input().split())
        conference.append((start, end))
    conference.sort(key = lambda x : (x[1],x[0]))

    cnt = 1
    end_t = conference[0][1]
    for i in range(1,N):
        if end_t <= conference[i][0]:
            cnt += 1
            end_t = conference[i][1]
    print(cnt)
if __name__ == '__main__':
    main()