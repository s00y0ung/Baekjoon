import sys
input = sys.stdin.readline

def binarySearch(s,f):
    left = 0
    right = len(N_list[f])-1

    while left <= right:
        mid = (left + right) // 2
        if s > N_list[f][mid]:
            left = mid + 1
        elif s < N_list[f][mid]:
            right = mid -1
        else:
            return True
    return False

N, M = map(int, input().split())
N_list = [[] for _ in range(26)]

for _ in range(N):
    n_str = input().rstrip()
    N_list[ord(n_str[0])-97].append(n_str)
for i in range(26):
    N_list[i].sort()
cnt = 0
for _ in range(M):
    m_str = input().rstrip()
    m_first = ord(m_str[0])-97
    if binarySearch(m_str, m_first):
        cnt += 1

print(cnt)