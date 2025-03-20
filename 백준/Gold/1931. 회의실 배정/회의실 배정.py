import sys
input = sys.stdin.readline

def binarySearch(search, idx):
    global meeting

    left = 0
    right = idx

    while left <= right:
        mid = (left + right) // 2

        if meeting[mid][1] > search:
            right = mid-1
        elif meeting[mid][1] <= search:
            left = mid + 1
    return right

if __name__ == "__main__":
    N = int(input())

    meeting = []
    for i in range(N):
        s, e = map(int, input().split())
        meeting.append([s,e,1])
    meeting.sort(key = lambda x : (x[1],x[0]))


    for idx in range(1,N):
        s,e,v = meeting[idx]

        exist = binarySearch(s, idx-1)
        if exist == -1:
            meeting[idx][2] = meeting[idx-1][2]
        else:
            meeting[idx][2] = max(1+meeting[exist][2], meeting[idx-1][2])

    print(meeting[N-1][2])
