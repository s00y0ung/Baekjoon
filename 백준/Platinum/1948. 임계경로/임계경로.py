import sys
input = sys.stdin.readline

def main():
    n = int(input())
    m = int(input())
    g = [[] for _ in range(n+1)]
    income = [0 for _ in range(n+1)]

    for _ in range(m):
        u,v,w = map(int, input().split())
        g[u].append([v,w])
        income[v] += 1

    s,e = map(int, input().split())
    que = [s]
    length = [0 for _ in range(n+1)]
    m_node = [[] for _ in range(n+1)]
    while que:
        cur = que.pop(0)
        for i,w in g[cur]:
            income[i] -= 1
            if length[i] < length[cur]+w:
                m_node[i] = [cur]
                length[i] = length[cur]+w
            elif length[i] == length[cur]+w:
                m_node[i].append(cur)

            if income[i] == 0:
                que.append(i)
    print(length[e]) #최대거리

    que = m_node[e]
    visited = [0 for _ in range(n+1)]
    ans = len(m_node[e])
    while que:
        cur = que.pop(0)
        if visited[cur] == 0:
            visited[cur] = 1
            ans += len(m_node[cur])
            for k in m_node[cur]:
                if visited[k] == 0:
                    que.append(k)
    print(ans) #색칠 도로의 수


if __name__ == '__main__':
    main()