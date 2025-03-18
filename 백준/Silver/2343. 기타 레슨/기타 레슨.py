def binarySearch(l,r):
    global lecture, M

    left = l
    right = r

    while left <= right:
        size = (left + right) // 2

        cnt = 0
        s = 0
        for l in lecture:
            if s+l > size:
                cnt += 1
                s = 0
            s += l
        if s!=0:
            cnt += 1

        if cnt <= M:
            right = size -1
        elif cnt > M:
            left = size + 1

    return left

if __name__ == "__main__":
    N, M = map(int,input().split())
    lecture = list(map(int, input().split()))

    print(binarySearch(max(lecture),sum(lecture)))