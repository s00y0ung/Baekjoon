import sys
import heapq
input = sys.stdin.readline

def main():
    n = int(input())
    m = int(input())
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int, input().split())
        g[u].append([v,w])
    s,e = map(int, input().split())

    heap = [(0,s)]
    distance = [float('inf')]*(n+1)
    distance[s] = 0
    while heap:
        dist, cur = heapq.heappop(heap)
        if distance[cur] < dist:
            if e == cur:
                break
            continue

        for i,w in g[cur]:
            if distance[i] > dist+w:
                distance[i] = dist+w
                heapq.heappush(heap,(dist+w, i))
    print(distance[e])


if __name__ == '__main__':
    main()