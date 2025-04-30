import sys
input = sys.stdin.readline 

N,M = map(int, input().split())

en_dic = {}

for idx in range(N):
    s = input().rstrip()
    if len(s) < M:
        continue
    if s in en_dic:
        en_dic[s][0] += 1
    else:
        en_dic[s] = [1,len(s),s] #나온 횟수, 단어 길이, 사전 순
s = sorted(en_dic.values(), key = lambda x : (-x[0],-x[1],x[2]))
for i in range(len(s)):
    print(s[i][2])