test_cnt = int(input())

st = list(input())
leng = len(st)
for _ in range(test_cnt-1):
    next_s = list(input())
    for s in range(leng):
        if next_s[s] != st[s]:
            st[s] = '?'
            
str = ''.join(st)
print(str)