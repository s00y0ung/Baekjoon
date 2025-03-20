import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    meeting = []
    for i in range(N):
        s, e = map(int, input().split())
        meeting.append([s,e])
    meeting.sort(key = lambda x : (x[1],x[0]))

    cnt = 0
    end = -1
    for i in range(N):
        if meeting[i][0] >= end:
            end = meeting[i][1]
            cnt += 1

    print(cnt)

