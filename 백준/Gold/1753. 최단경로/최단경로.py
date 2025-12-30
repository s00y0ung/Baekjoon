import sys,heapq
input = sys.stdin.readline

def main():
    V,E = map(int, input().split())
    start = int(input())

    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a,b,w = map(int, input().split())
        graph[a].append((b,w))

    distance = [10000000]*(V+1)
    distance[start] = 0

    h = [(0,start)]
    while h:
        dist, cur = heapq.heappop(h)
        if distance[cur] < dist:
            continue

        for i,w in graph[cur]:
            if distance[i] > distance[cur]+w:
                distance[i] = distance[cur]+w
                heapq.heappush(h,(distance[i],i))

    for d in distance[1:]:
        if d == 10000000: print("INF")
        else: print(d)

if __name__ == "__main__":
    main()