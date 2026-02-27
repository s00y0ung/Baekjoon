import sys
import heapq
input = sys.stdin.readline

def main():
    N = int(input())
    h = []
    for _ in range(N):
        h.append(int(input()))
    heapq.heapify(h)

    ans = 0
    while len(h) > 1:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        ans = (ans+a+b)
        heapq.heappush(h,a+b)
    print(ans)

if __name__ == "__main__":
    main()