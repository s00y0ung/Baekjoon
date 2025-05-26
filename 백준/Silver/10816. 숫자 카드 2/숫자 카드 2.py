import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
finds = list(map(int, input().split()))

cards_dic = {}
for c in cards:
    if c in cards_dic:
        cards_dic[c] += 1
    else:
        cards_dic[c] = 1

ans = []
for f in finds:
    if f in cards_dic:
        ans.append(cards_dic[f])
    else:
        ans.append(0)
print(*ans)
