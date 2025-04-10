import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = [[] for _ in range(26)]

for _ in range(N):
    n_str = input().rstrip()
    N_list[ord(n_str[0])-97].append(n_str)
    
cnt = 0
for _ in range(M):
    m_str = input().rstrip()
    m_first = ord(m_str[0])-97
    if m_str in N_list[m_first]:
        cnt += 1

print(cnt)