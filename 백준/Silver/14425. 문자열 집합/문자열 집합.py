import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = set()
for _ in range(N):
    N_list.add(input().rstrip())

cnt = 0
for _ in range(M):
    m_str = input().rstrip()
    if m_str in N_list:
        cnt += 1

print(cnt)