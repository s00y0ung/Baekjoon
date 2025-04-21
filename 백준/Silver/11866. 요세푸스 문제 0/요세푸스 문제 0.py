N, K = map(int, input().split())
q = [i for i in range(1, N+1)]

s = -1
q_size = N
q_list = []
for _ in range(N):
    q_list.append(str(q.pop((s+K)%q_size)))
    s = (s+K)%q_size - 1
    q_size -= 1
print("<"+', '.join(q_list)+">")